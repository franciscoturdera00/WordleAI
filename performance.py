import os
from enum import Enum
from pathlib import Path
import json
from tqdm import tqdm

from config.performance_parser import performance_parser
from game_logic.ai_play import play_ai
from util.functions import get_official_list, generate_word_from, get_all_5_letter_words

PERFORMANCE_MARKER = 2000
current_path = str(Path(os.getcwd()))


class Strats(Enum):
    SIMPLE_FILTER_OFFICIAL = 'simple_filter_official'
    SIMPLE_FILTER_ALL_5 = 'simple_filter_all_5'
    SMART_GUESS_OFFICIAL = 'smart_guess_official'
    SMART_GUESS_ALL_5 = 'smart_guess_all_5'
    INDEX_DECISION_OFFICIAL = 'index_decision_official'
    INDEX_DECISION_ALL_5 = 'index_decision_all_5'


def identity_or_progress(progress, fn):
    if progress:
        return tqdm(fn)
    return fn


def test_performance(strategy, word_bank, secret_bank, performance_marker, print_mode):
    _, average = play_ai(strategy, word_bank.copy(), secret_bank, generate_word_from(word_bank.copy()), 6000)
    for i in identity_or_progress(print_mode, range(2, performance_marker)):
        _, num = play_ai(strategy, word_bank.copy(), secret_bank, generate_word_from(word_bank.copy()), 6000)
        average = ((i - 1) * average + num) / i
    return average


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
    lst = get_all_5_letter_words(current_path)
    return test_performance("index_decision", lst, set(), PERFORMANCE_MARKER, print_mode)


def display_performance(strategy, lst, average):
    print(strategy + " with " + lst + " Average Number of Attempts: " + str(average))


def run_all(print_mode):
    value = test_simple_filter_performance_with_official_wordle_list(print_mode)
    if args.update_analytics:
        update_performance_analytics(averages, Strats.SIMPLE_FILTER_OFFICIAL.value, value)
    display_performance("Simple Filter", "Official Wordle List", value)

    value = test_simple_filter_performance_with_all_5_letter_words(print_mode)
    if args.update_analytics:
        update_performance_analytics(averages, Strats.SIMPLE_FILTER_ALL_5.value, value)
    display_performance("Simple Filter", "all 5 letter word list", value)

    value = test_smart_guess_with_official_wordle_list(print_mode)
    if args.update_analytics:
        update_performance_analytics(averages, Strats.SMART_GUESS_OFFICIAL.value, value)
    display_performance("Smart Guess", "Official Wordle List", value)

    value = test_smart_guess_with_all_5_letter_words(print_mode)
    if args.update_analytics:
        update_performance_analytics(averages, Strats.SMART_GUESS_ALL_5.value, value)
    display_performance("Smart Guess", "all 5 letter word list", value)

    value = test_index_decision_with_official_wordle_list(print_mode)
    if args.update_analytics:
        update_performance_analytics(averages, Strats.INDEX_DECISION_OFFICIAL.value, value)
    display_performance("Index Decision", "Official Wordle List", value)

    value = test_index_decision_with_all_5_letter_words(print_mode)
    if args.update_analytics:
        update_performance_analytics(averages, Strats.INDEX_DECISION_ALL_5.value, value)
    display_performance("Index Decision", "all 5 letter word list", value)


def update_performance_analytics(jsn, strategy, updated_value):
    jsn[strategy] = updated_value


if __name__ == '__main__':
    args = performance_parser()
    not_valid = True
    analytics_file = 'performance_analytics/analytics.json'
    if args.update_analytics:
        with open(analytics_file) as json_file:
            averages = json.load(json_file)
    print("Testing Performance")
    if args.strategy is None or not args.strategy:
        run_all(args.show_progress)
    else:
        if Strats.SIMPLE_FILTER_OFFICIAL.value in args.strategy:
            new_value = test_simple_filter_performance_with_official_wordle_list(args.show_progress)
            if args.update_analytics:
                update_performance_analytics(averages, Strats.SIMPLE_FILTER_OFFICIAL.value, new_value)
            display_performance("Simple Filter", "Official Wordle_List", new_value)
            not_valid = False
        if Strats.SIMPLE_FILTER_ALL_5.value in args.strategy:
            new_value = test_simple_filter_performance_with_all_5_letter_words(args.show_progress)
            if args.update_analytics:
                update_performance_analytics(averages, Strats.SIMPLE_FILTER_ALL_5.value, new_value)
            display_performance("Simple Filter", "all 5 letter word list", new_value)
            not_valid = False
        if Strats.SMART_GUESS_OFFICIAL.value in args.strategy:
            new_value = test_smart_guess_with_official_wordle_list(args.show_progress)
            if args.update_analytics:
                update_performance_analytics(averages, Strats.SMART_GUESS_OFFICIAL.value, new_value)
            display_performance("Smart Guess", "Official Wordle List", new_value)
            not_valid = False
        if Strats.SMART_GUESS_ALL_5.value in args.strategy:
            new_value = test_smart_guess_with_all_5_letter_words(args.show_progress)
            if args.update_analytics:
                update_performance_analytics(averages, Strats.SMART_GUESS_ALL_5.value, new_value)
            display_performance("Smart Guess", "all 5 letter word list", new_value)
            not_valid = False
        if Strats.INDEX_DECISION_OFFICIAL.value in args.strategy:
            new_value = test_index_decision_with_official_wordle_list(args.show_progress)
            if args.update_analytics:
                update_performance_analytics(averages, Strats.INDEX_DECISION_OFFICIAL.value, new_value)
            display_performance("Index Decision", "Official Wordle List", new_value)
            not_valid = False
        if Strats.INDEX_DECISION_ALL_5.value in args.strategy:
            new_value = test_index_decision_with_all_5_letter_words(args.show_progress)
            if args.update_analytics:
                update_performance_analytics(averages, Strats.INDEX_DECISION_ALL_5.value, new_value)
            display_performance("Index Decision", "all 5 letter word list", new_value)
            not_valid = False
        if not_valid:
            exit("Not a valid request")

    # Writes updated json to file
    if args.update_analytics:
        with open(analytics_file, 'w') as f:
            json.dump(averages, f, indent=4)
