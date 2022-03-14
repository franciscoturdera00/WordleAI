import random

from strategies.feedback import Feedback


def get_word_list_from(path):
    with open(path) as f:
        official_list = [x.replace("\n", "") for x in f.readlines()]
    return set(official_list)


def get_official_list(path):
    return get_word_list_from(path + "/word_banks/wordle_official_list.txt")


def get_all_5_letter_words(path):
    return get_word_list_from(path + "/word_banks/5_letters.txt")


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
    return random.choice(list(word_bank))


def quantity_ordered_list(integer_value_map):
    """Returns ordered list in format: [(key34, 86), (key89, 53), (key12, 42)...]"""
    final_list = []
    for key in integer_value_map:
        final_list.append((key, integer_value_map[key]))
    final_list.sort(key=lambda x: x[1], reverse=True)
    return final_list
