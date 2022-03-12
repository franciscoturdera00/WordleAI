import string
import argparse

from strategies.basic_filter import BasicFilterStrategy
from strategies.feedback import Feedback
from strategies.random_strategy import RandomStrategy

list_of_letters = list(string.ascii_lowercase)


def play(strat_type, word_bank, answer, attempts_left, print_mode=False):
    strategy = choose_strategy(strat_type, word_bank, len(answer))
    max_attempts = attempts_left
    while attempts_left > 0:
        guess = strategy.guess()
        attempts_left -= 1
        if guess == answer:
            return True, max_attempts - attempts_left
        feedback = analyze_guess(guess, answer)
        strategy.feedback(guess, feedback)
        if print_mode:
            print_progress(guess, feedback)
    return False, max_attempts


def choose_strategy(strategy, word_bank, answer_length):
    if strategy == "random":
        return RandomStrategy(word_bank, answer_length)
    if strategy == "dumb_filter":
        return BasicFilterStrategy(word_bank, answer_length)
    else:
        exit("No valid strategy")


def analyze_guess(guess, answer):
    """Returns information of the guess in relation to the correct answer"""
    feedback = [None] * len(answer)
    correct_found = dict.fromkeys(list_of_letters, 0)
    for i, c in enumerate(answer):
        if guess[i] == c:
            feedback[i] = Feedback.CORRECT
            correct_found[c] += 1
    for i, c in enumerate(answer):
        if guess[i] == c:
            continue
        if guess[i] in answer and correct_found[guess[i]] < answer.count(guess[i]):
            feedback[i] = Feedback.IN_WORD
    for i, c in enumerate(answer):
        if feedback[i] is None:
            feedback[i] = Feedback.NOT_IN_WORD
    return feedback


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


def initiate_parser():
    parser = argparse.ArgumentParser(description='Wordle AI')
    parser.add_argument('-s', '--strategy', dest='strategy', nargs='?', default='random', const='random',
                        type=str, help='Strategy used in the game. Options include: random, dumb_filter')
    parser.add_argument('-wb', '--wordbank', dest='word_bank', nargs='?', default="word_banks/test.txt",
                        const="word_banks/test.txt", type=str, help="File Path for word bank to be used")
    parser.add_argument('-w', '--word', dest='word', type=str, required=True, help='Word to guess')
    parser.add_argument('-a', '--attempts', dest='attempts', nargs='?', default=6, const=6, type=int,
                        help='Attempts the AI receives')
    parser.add_argument('-p', '--print', dest='print_mode', action='store_true', default=False,
                        help='Print progress of AI as it makes guesses')

    return parser.parse_args()


if __name__ == '__main__':
    args = initiate_parser()
    win, attempts = play(args.strategy, args.word_bank, args.word, args.attempts, args.print_mode)
    # win, attempts = play("random", "word_banks/5_letters.txt", word, 6, True)
    if win:
        print("Win in %d attempts! Word: %s" % (attempts, args.word))
    else:
        print("Lose :( Word: %s" % args.word)
