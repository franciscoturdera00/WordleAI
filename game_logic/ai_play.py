from game_logic.analyzer import analyze_guess
from strategies.strategy import Strategy
from util.functions import print_progress


def play_game(
    strategy: Strategy,
    word_bank: set,
    secret_bank: set,
    answer: str,
    attempts_left: int,
    print_mode=False,
    never_lose=False,
):
    if answer not in word_bank:
        raise ValueError("Answer is not in Word Bank")
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


def game(strategy: Strategy, wb: set, sb: set, answer: str, attempts: int, print_mode):
    win, attempts = False, attempts
    try:
        win, attempts = play_game(strategy, wb, sb, answer.lower(), attempts, print_mode=print_mode)
    except ValueError as ve:
        exit(str(ve))
    if win:
        print("Win in %d attempts! Word: %s" % (attempts, answer))
    else:
        print("Lose :( Word: %s" % answer)

