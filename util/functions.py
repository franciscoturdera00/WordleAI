import os
import random
from pathlib import Path

from strategies.feedback import Feedback


def get_parent_path():
    path = Path(os.getcwd())
    return str(path.parent.absolute())


def get_word_list_from(path):
    with open(path) as f:
        official_list = [x.replace("\n", "") for x in f.readlines()]
    return set(official_list)


def get_official_list():
    return get_word_list_from(get_parent_path() + "/word_banks/wordle_official_list.txt")


def get_all_5_letter_words():
    return get_word_list_from(get_parent_path() + "/word_banks/5_letters.txt")


def print_progress(guess, feedback):
    """Prints progress of game"""
    guess_status = ""
    for _, el in enumerate(feedback):
        if el == Feedback.NOT_IN_WORD:
            guess_status += "X"
        elif el == Feedback.IN_WORD:
            guess_status += "@"
        elif el == Feedback.CORRECT:
            guess_status += "$"
    print(guess)
    print(guess_status)
    print()


def generate_word_from(word_bank):
    return random.sample(word_bank, 1)[0]
