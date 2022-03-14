from game_logic.analyzer import analyze_guess
from strategies.index_decision import IndexDecisionStrategy
from strategies.random_strategy import RandomStrategy
from strategies.simple_filter import SimpleFilterStrategy
from strategies.smart_guess import SmartGuessStrategy
from util.functions import print_progress


def play_ai(strat_type, word_bank, answer, attempts_left, print_mode=False):
    if answer not in word_bank:
        exit("Answer is not in Word Bank")
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
    if strategy == "simple_filter":
        return SimpleFilterStrategy(word_bank, answer_length)
    if strategy == "smart_guess":
        return SmartGuessStrategy(word_bank, answer_length)
    if strategy == "index_decision":
        return IndexDecisionStrategy(word_bank, answer_length)
    else:
        exit("Not a valid strategy")
