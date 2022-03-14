import os
from pathlib import Path

from config.performance_parser import performance_parser
from game_logic.ai_play import play_ai
from util.functions import get_official_list, generate_word_from, get_all_5_letter_words

PERFORMANCE_MARKER = 1000
current_path = str(Path(os.getcwd()))


def test_performance(strategy, word_bank, performance_marker, print_mode=False):
    _, average = play_ai(strategy, word_bank.copy(), generate_word_from(word_bank.copy()), 6000)
    for i in range(2, performance_marker):
        if print_mode and i % 50 == 0:
            print(".", end="")
        _, num = play_ai(strategy, word_bank.copy(), generate_word_from(word_bank.copy()), 6000)
        average = ((i - 1) * average + num) / i
    if print_mode:
        print()
    return average


def test_simple_filter_performance_with_official_wordle_list(print_mode=False):
    official_list = get_official_list(current_path)
    return test_performance("simple_filter", official_list, PERFORMANCE_MARKER, print_mode)


def test_simple_filter_performance_with_all_5_letter_words(print_mode=False):
    lst = get_all_5_letter_words(current_path)
    return test_performance("simple_filter", lst, PERFORMANCE_MARKER, print_mode)


def test_smart_guess_with_official_wordle_list(print_mode=False):
    official_list = get_official_list(current_path)
    return test_performance("smart_guess", official_list, PERFORMANCE_MARKER, print_mode)


def test_smart_guess_with_all_5_letter_words(print_mode=False):
    lst = get_all_5_letter_words(current_path)
    return test_performance("smart_guess", lst, PERFORMANCE_MARKER, print_mode)


def display_performance(strategy, average):
    print(strategy + " with Official Wordle List Average Number of Attempts: " + str(average))


def run_all():
    print("Testing Performance")
    display_performance("Simple Filter", test_simple_filter_performance_with_official_wordle_list(True))
    display_performance("Simple Filter", test_simple_filter_performance_with_all_5_letter_words(True))
    display_performance("Smart Guess", test_smart_guess_with_official_wordle_list(True))
    display_performance("Smart Guess", test_smart_guess_with_all_5_letter_words(True))


if __name__ == '__main__':
    args = performance_parser()
    if args.strategy is None:
        run_all()
    else:
        print("Testing Performance")
        if args.strategy == 'simple_filter_official':
            display_performance("Simple Filter", test_simple_filter_performance_with_official_wordle_list(True))
        elif args.strategy == 'simple_filter_all_5':
            display_performance("Simple Filter", test_simple_filter_performance_with_all_5_letter_words(True))
        elif args.strategy == "smart_guess_official":
            display_performance("Smart Guess", test_smart_guess_with_official_wordle_list(True))
        elif args.strategy == "smart_guess_all_5":
            display_performance("Smart Guess", test_smart_guess_with_all_5_letter_words(True))
        else:
            exit("Not a valid request")
