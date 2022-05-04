#!/usr/bin/env python3

import os
from pathlib import Path

from config.manual_play_parser import manual_parser
from game_logic.analyzer import analyze_guess
from util.functions import (
    get_official_list,
    print_progress,
    get_word_list_from,
    generate_word_from,
    get_official_guess_list,
)


def play_game(path, args):
    if args.word_bank is None:
        word_bank = list(get_official_list(path))
    else:
        word_bank = list(get_word_list_from(args.word_bank))
    if args.secret_bank is None:
        secret_bank = set(get_official_guess_list(path))
    else:
        secret_bank = get_word_list_from(args.secret_bank)
    answer = generate_word_from(word_bank)
    word_bank = set(word_bank)
    total_attempts = args.attempts
    attempts = args.attempts
    error_input = True
    guess = ""
    while guess != answer and attempts > 0:
        while error_input:
            try:
                guess = input("Guess: ")
                print()
                feedback = analyze_guess(guess, answer, word_bank, secret_bank)
                print_progress(guess, feedback)
                word_bank.discard(guess)
                secret_bank.discard(guess)
                attempts -= 1
                print("Attempts left: %d" % attempts)
                error_input = False
            except ValueError as e:
                print("Invalid guess, try again, " + str(e))
        error_input = True
    if guess == answer:
        print()
        print("Correct! You won in %d attempts!" % (total_attempts - attempts))
    else:
        print()
        print("You Lost :( The word was %s" % answer)


if __name__ == "__main__":
    arguments = manual_parser()
    print("Welcome to Wordle!")
    print()
    print("'X' means the letter is not in the word")
    print("'@' means the letter is in the word, but not in the correct spot")
    print("'$' means you are right on the money! This letter is in this spot")
    print()
    print("Let's Begin!")
    print()
    current_path = str(Path(os.getcwd()))
    while True:
        play_game(current_path, arguments)
        play_again = ""
        while play_again != "y" and play_again != "n":
            play_again = input("Want to play again? (y/n) ")
            if play_again == "y":
                print()
                print("Let's play again!")
                print()
                break
            elif play_again == "n":
                print()
                exit("Thanks for playing!")
            else:
                print("Please input 'y' ot 'n'")
                continue
