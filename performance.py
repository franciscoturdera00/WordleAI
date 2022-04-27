#!/usr/bin/env python3

import os
from pathlib import Path
import json
from tqdm import tqdm

from config.performance_parser import performance_parser
from game_logic.ai_play import play_ai
from util.functions import get_official_list, generate_word_from, get_all_5_letter_words, get_official_guess_list, \
    get_simplified_5_list, remove_0s, quantity_ordered_list
from util.meta_enum import BaseEnum

PERFORMANCE_MARKER = 2000
current_path = str(Path(os.getcwd()))


class Strats(BaseEnum):
    SIMPLE_FILTER_OFFICIAL = 'simple_filter_official'
    SIMPLE_FILTER_ALL_5 = 'simple_filter_all_5'
    SMART_GUESS_OFFICIAL = 'smart_guess_official'
    SMART_GUESS_ALL_5 = 'smart_guess_all_5'
    INDEX_DECISION_OFFICIAL = 'index_decision_official'
    INDEX_DECISION_ALL_5 = 'index_decision_all_5'
    OUTSIDE_THE_BOX_OFFICIAL = "outside_the_box_official"
    OUTSIDE_THE_BOX_LARGE = "outside_the_box_large"
    MARKOV_OFFICIAL = "markov_official"


def identity_or_progress(progress, fn):
    if progress:
        return tqdm(fn)
    return fn


def test_performance(strategy, word_bank, secret_bank, performance_marker, print_mode):
    average = 0
    frequency = dict.fromkeys(range(1, 10000), 0)
    for i in identity_or_progress(print_mode, range(1, performance_marker + 1)):
        _, num = play_ai(strategy, word_bank.copy(), secret_bank.copy(), generate_word_from(word_bank.copy()), 6000)
        average = ((i - 1) * average + num) / i
        frequency[num] += 1
    frequency = remove_0s(frequency)
    ordered = quantity_ordered_list(frequency)
    mean = ordered[0][0]
    return average, mean, frequency


def test_simple_filter_performance_with_official_wordle_list(print_mode):
    official_list = get_official_list(current_path)
    return test_performance("simple_filter", official_list, set(), PERFORMANCE_MARKER, print_mode)


def test_simple_filter_performance_with_all_5_letter_words(print_mode):
    lst = get_all_5_letter_words(current_path)
    return test_performance("simple_filter", lst, set(), PERFORMANCE_MARKER, print_mode)


def test_smart_guess_with_official_wordle_list(print_mode):
    official_list = get_official_list(current_path)
    return test_performance("smart_guess", official_list, set(), PERFORMANCE_MARKER, print_mode)


def test_smart_guess_with_all_5_letter_words(print_mode):
    lst = get_all_5_letter_words(current_path)
    return test_performance("smart_guess", lst, set(), PERFORMANCE_MARKER, print_mode)


def test_index_decision_with_official_wordle_list(print_mode):
    official_list = get_official_list(current_path)
    return test_performance("index_decision", official_list, set(), PERFORMANCE_MARKER, print_mode)


def test_index_decision_with_all_5_letter_words(print_mode):
    lst = get_simplified_5_list(current_path)
    return test_performance("index_decision", lst, set(), PERFORMANCE_MARKER, print_mode)


def test_out_the_box_with_official_wordle_list(print_mode):
    official_list = get_official_list(current_path)
    secret_list = get_official_guess_list(current_path)
    return test_performance("outside_the_box", official_list, secret_list, PERFORMANCE_MARKER, print_mode)


def test_out_the_box_with_simplified_5_list(print_mode):
    simplified_5 = get_simplified_5_list(current_path)
    secret_list = get_all_5_letter_words(current_path)
    return test_performance("outside_the_box", simplified_5, secret_list, PERFORMANCE_MARKER, print_mode)


def test_markov_with_official_wordle_list(print_mode):
    official_list = get_official_list(current_path)
    return test_performance("markov", official_list, set(), PERFORMANCE_MARKER, print_mode)


def display_performance(strategy, lst, dt):
    print(strategy + " with " + lst)
    print("Average Number of Attempts: " + str(dt[0]))
    print("Mean Number of Attempts: " + str(dt[1]))
    print("Break Down: " + str(dt[2]))


def run_all(print_mode, d, u_a):
    handle_simple_filter_official(print_mode, d, u_a)
    handle_simple_filter_all_5(print_mode, d, u_a)
    handle_smart_guess_official(print_mode, d, u_a)
    handle_smart_guess_all_5(print_mode, d, u_a)
    handle_index_decision_official(print_mode, d, u_a)
    handle_index_decision_all_5(print_mode, d, u_a)
    handle_outside_the_box_official(print_mode, d, u_a)
    handle_outside_the_box_large(print_mode, d, u_a)
    handle_markov_official(print_mode, d, u_a)


def handle_simple_filter_official(print_mode, data, update):
    new_value = test_simple_filter_performance_with_official_wordle_list(print_mode)
    if update:
        update_performance_analytics(data, Strats.SIMPLE_FILTER_OFFICIAL.value, new_value)
    display_performance("Simple Filter", "Official Wordle List", new_value)


def handle_simple_filter_all_5(print_mode, data, update):
    new_value = test_simple_filter_performance_with_all_5_letter_words(print_mode)
    if update:
        update_performance_analytics(data, Strats.SIMPLE_FILTER_ALL_5.value, new_value)
    display_performance("Simple Filter", "all 5 letter word list", new_value)


def handle_smart_guess_official(print_mode, data, update):
    new_value = test_smart_guess_with_official_wordle_list(print_mode)
    if update:
        update_performance_analytics(data, Strats.SMART_GUESS_OFFICIAL.value, new_value)
    display_performance("Smart Guess", "Official Wordle List", new_value)


def handle_smart_guess_all_5(print_mode, data, update):
    new_value = test_smart_guess_with_all_5_letter_words(print_mode)
    if update:
        update_performance_analytics(data, Strats.SMART_GUESS_ALL_5.value, new_value)
    display_performance("Smart Guess", "all 5 letter word list", new_value)


def handle_index_decision_official(print_mode, data, update):
    new_value = test_index_decision_with_official_wordle_list(print_mode)
    if update:
        update_performance_analytics(data, Strats.INDEX_DECISION_OFFICIAL.value, new_value)
    display_performance("Index Decision", "Official Wordle List", new_value)


def handle_index_decision_all_5(print_mode, data, update):
    new_value = test_index_decision_with_all_5_letter_words(print_mode)
    if update:
        update_performance_analytics(data, Strats.INDEX_DECISION_ALL_5.value, new_value)
    display_performance("Index Decision", "all 5 letter word list", new_value)


def handle_outside_the_box_official(print_mode, data, update):
    new_value = test_out_the_box_with_official_wordle_list(print_mode)
    if update:
        update_performance_analytics(data, Strats.OUTSIDE_THE_BOX_OFFICIAL.value, new_value)
    display_performance("Think Outside The Box", "Official Wordle List with Official Guess List", new_value)


def handle_outside_the_box_large(print_mode, data, update):
    new_value = test_out_the_box_with_simplified_5_list(print_mode)
    if update:
        update_performance_analytics(data, Strats.OUTSIDE_THE_BOX_LARGE.value, new_value)
    display_performance("Think Outside The Box", "Large 5-Letter List with all 5 letters Guess List", new_value)


def handle_markov_official(print_mode, data, update):
    new_value = test_markov_with_official_wordle_list(print_mode)
    if update:
        update_performance_analytics(data, Strats.MARKOV_OFFICIAL, new_value)
    display_performance("Markov", "Official Wordle List", new_value)


def update_performance_analytics(jsn, strategy, updated_value):
    jsn['Performance'][strategy]['average'] = updated_value[0]
    jsn['Performance'][strategy]['mean'] = updated_value[1]
    jsn['Performance'][strategy]['break_down'] = updated_value[2]


if __name__ == '__main__':
    args = performance_parser()
    if args.strategy is not None and not Strats.__contains_all__(args.strategy):
        exit("Invalid Strategy Given")
    not_valid = True
    analytics_file = 'performance_analytics/analytics.json'
    db = None
    if args.update_analytics:
        with open(analytics_file) as json_file:
            db = json.load(json_file)
    print("Testing Performance")
    if args.strategy is None or not args.strategy:
        run_all(args.show_progress, db, args.update_analytics)
    else:
        if Strats.SIMPLE_FILTER_OFFICIAL.value in args.strategy:
            handle_simple_filter_official(args.show_progress, db, args.update_analytics)
            not_valid = False

        if Strats.SIMPLE_FILTER_ALL_5.value in args.strategy:
            handle_simple_filter_all_5(args.show_progress, db, args.update_analytics)
            not_valid = False

        if Strats.SMART_GUESS_OFFICIAL.value in args.strategy:
            handle_smart_guess_official(args.show_progress, db, args.update_analytics)
            not_valid = False

        if Strats.SMART_GUESS_ALL_5.value in args.strategy:
            handle_smart_guess_all_5(args.show_progress, db, args.update_analytics)
            not_valid = False

        if Strats.INDEX_DECISION_OFFICIAL.value in args.strategy:
            handle_index_decision_official(args.show_progress, db, args.update_analytics)
            not_valid = False

        if Strats.INDEX_DECISION_ALL_5.value in args.strategy:
            handle_index_decision_all_5(args.show_progress, db, args.update_analytics)
            not_valid = False

        if Strats.OUTSIDE_THE_BOX_OFFICIAL.value in args.strategy:
            handle_outside_the_box_official(args.show_progress, db, args.update_analytics)
            not_valid = False

        if Strats.OUTSIDE_THE_BOX_LARGE.value in args.strategy:
            handle_outside_the_box_large(args.show_progress, db, args.update_analytics)
            not_valid = False

        if Strats.MARKOV_OFFICIAL.value in args.strategy:
            handle_markov_official(args.show_progress, db, args.update_analytics)
            not_valid = False

        if not_valid:
            exit("Not a valid request")

    # Writes updated json to file
    if args.update_analytics:
        with open(analytics_file, 'w') as f:
            json.dump(db, f, indent=4)
