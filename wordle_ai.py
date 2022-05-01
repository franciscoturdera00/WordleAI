#!/usr/bin/env python3

from config.arguments_parser import initiate_parser
from game_logic.ai_play import play_ai


def ai_plays(args, wb, sb):
    win, attempts = False, args.attempts
    try:
        win, attempts = play_ai(
            args.strategy.lower(),
            wb,
            sb,
            args.word.lower(),
            args.attempts,
            print_mode=args.print_mode,
        )
    except ValueError as ve:
        exit(str(ve))
    if win:
        print("Win in %d attempts! Word: %s" % (attempts, args.word))
    else:
        print("Lose :( Word: %s" % args.word)


if __name__ == "__main__":
    arguments = initiate_parser()
    secret_bank = set()
    try:
        with open(arguments.word_bank) as f:
            word_bank = set([x.replace("\n", "").lower() for x in f.readlines()])
        if arguments.secret_bank is not None:
            with open(arguments.secret_bank) as g:
                secret_bank = set([x.replace("\n", "").lower() for x in g.readlines()])
    except OSError as e:
        exit(str(e))
    ai_plays(arguments, word_bank, secret_bank)
