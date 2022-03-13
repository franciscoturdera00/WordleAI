from util.functions import choose_strategy, analyze_guess, print_progress


def play_ai(strat_type, word_bank, answer, attempts_left, print_mode=False):
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
