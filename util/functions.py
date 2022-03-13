import os
from pathlib import Path

from strategies.feedback import Feedback
from strategies.random_strategy import RandomStrategy
from strategies.simple_filter import SimpleFilterStrategy
from util.constants import LIST_OF_LETTERS


def get_parent_path():
    path = Path(os.getcwd())
    return str(path.parent.absolute())


def get_official_list():
    with open(get_parent_path() + "/word_banks/wordle_official_list.txt") as f:
        official_list = [x.replace("\n", "") for x in f.readlines()]
    return set(official_list)


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


def choose_strategy(strategy, word_bank, answer_length):
    if strategy == "random":
        return RandomStrategy(word_bank, answer_length)
    if strategy == "simple_filter":
        return SimpleFilterStrategy(word_bank, answer_length)
    else:
        exit("Not a valid strategy")


def analyze_guess(guess, answer):
    """Returns information of the guess in relation to the correct answer"""
    if len(guess) != len(answer):
        exit("Word Bank or Word contains wrong length words")
    feedback = [Feedback.NOT_IN_WORD] * len(answer)
    correct_found = dict.fromkeys(LIST_OF_LETTERS, 0)
    letter_found = dict.fromkeys(LIST_OF_LETTERS, 0)
    for i, c in enumerate(answer):
        if guess[i] == c:
            feedback[i] = Feedback.CORRECT
            correct_found[c] += 1
    for i, c in enumerate(answer):
        if guess[i] == c:
            continue
        if guess[i] in answer and correct_found[guess[i]] + letter_found[guess[i]] < answer.count(guess[i]):
            feedback[i] = Feedback.IN_WORD
            letter_found[guess[i]] += 1
    return feedback
