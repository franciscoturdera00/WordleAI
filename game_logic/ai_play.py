from game_logic.analyzer import analyze_guess
from strategies.index_decision import IndexDecisionStrategy
from strategies.markov import MarkovStrategy
from strategies.outside_the_box import ThinkOutsideTheBoxStrategy
from strategies.random_strategy import RandomStrategy
from strategies.simple_filter import SimpleFilterStrategy
from strategies.smart_guess import SmartGuessStrategy
from util.functions import print_progress


def play_ai(
    strat_type,
    word_bank,
    secret_bank,
    answer,
    attempts_left,
    print_mode=False,
    never_lose=False,
):
    if answer not in word_bank:
        raise ValueError("Answer is not in Word Bank")
    strategy = choose_strategy(
        strat_type, word_bank.copy(), secret_bank.copy(), len(answer), attempts_left
    )
    max_attempts = attempts_left
    while attempts_left > 0 or never_lose:
        guess = strategy.guess()
        attempts_left -= 1
        if guess == answer:
            return True, max_attempts - attempts_left
        try:
            feedback = analyze_guess(guess, answer, word_bank, secret_bank)
        except ValueError as e:
            raise e
        word_bank.discard(guess)
        secret_bank.discard(guess)
        strategy.feedback(guess, feedback)
        if print_mode:
            print_progress(guess, feedback)
    return False, max_attempts


def choose_strategy(strategy, word_bank, secret_bank, answer_length, attempts):
    if strategy == "random":
        return RandomStrategy(word_bank, secret_bank, answer_length, attempts)
    if strategy == "simple_filter":
        return SimpleFilterStrategy(word_bank, secret_bank, answer_length, attempts)
    if strategy == "smart_guess":
        return SmartGuessStrategy(word_bank, secret_bank, answer_length, attempts)
    if strategy == "index_decision":
        return IndexDecisionStrategy(word_bank, secret_bank, answer_length, attempts)
    if strategy == "outside_the_box":
        return ThinkOutsideTheBoxStrategy(
            word_bank, secret_bank, answer_length, attempts
        )
    if strategy == "markov":
        return MarkovStrategy(word_bank, secret_bank, answer_length, attempts)
    else:
        exit("Not a valid strategy")
