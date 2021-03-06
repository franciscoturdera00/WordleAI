import random

from strategies.feedback import Feedback
from itertools import product
from colorama import Fore


def get_word_list_from(path):
    try:
        with open(path) as f:
            official_list = [x.replace("\n", "") for x in f.readlines()]
    except OSError:
        raise OSError("Path %s does not exist" % path)
    return set(official_list)


def get_official_list(path):
    return get_word_list_from(path + "/word_banks/wordle_official_list.txt")


def get_official_guess_list(path):
    return get_word_list_from(path + "/word_banks/official_allowed_guesses.txt")


def get_all_5_letter_words(path):
    return get_word_list_from(path + "/word_banks/5_letters.txt")


def get_simplified_5_list(path):
    return get_word_list_from(path + "/word_banks/simplified_5.txt")


def print_progress(guess, feedback):
    """Prints progress of game"""
    guess_status = ""
    for _, el in enumerate(feedback):
        if el == Feedback.NOT_IN_WORD:
            guess_status += Fore.RED + "X"
        elif el == Feedback.IN_WORD:
            guess_status += Fore.YELLOW + "@"
        elif el == Feedback.CORRECT:
            guess_status += Fore.GREEN + "$"
    guess_status += Fore.WHITE
    print(guess)
    print(guess_status)
    print()


def generate_word_from(word_bank):
    return random.choice(list(word_bank))


def quantity_ordered_list(integer_value_map, log=None):
    """Returns ordered list in format: [(key34, 86), (key89, 53), (key12, 42)...]"""
    final_list = []
    for key in integer_value_map:
        if log is None:
            final_list.append((key, integer_value_map[key]))
        else:
            final_list.append((key, integer_value_map[key], log))
    final_list.sort(key=lambda x: x[1], reverse=True)
    return final_list


def flatten(list_of_lists):
    return [item for sublist in list_of_lists for item in sublist]


def remove_0s(original):
    return {ch: freq for ch, freq in original.items() if freq != 0}


def flip_weighted_coin(cutoff=0.5):
    val = random.uniform(0, 1)
    return val < cutoff


def get_product(size, *candidates):
    return list(product(list(candidates), repeat=size))
