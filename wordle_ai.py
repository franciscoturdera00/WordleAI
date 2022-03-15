from config.arguments_parser import initiate_parser
from game_logic.ai_play import play_ai


def ai_plays(args, words, secrets):
    win = False
    attempts = args.attempts
    try:
        win, attempts = play_ai(args.strategy.lower(), words, secrets,
                                args.word.lower(), args.attempts, args.print_mode)
    except ValueError as e:
        exit(str(e))
    if win:
        print("Win in %d attempts! Word: %s" % (attempts, args.word))
    else:
        print("Lose :( Word: %s" % args.word)


if __name__ == '__main__':
    arguments = initiate_parser()
    try:
        with open(arguments.word_bank) as f:
            word_bank = set([x.replace("\n", "").lower() for x in f.readlines()])
    except OSError:
        exit("Word Bank Path does not exist")

    secret_bank = set()
    if arguments.secret_bank is not None:
        try:
            with open(arguments.secret_bank) as f:
                secret_bank = set([x.replace("\n", "").lower() for x in f.readlines()])
        except OSError:
            exit("Secret Bank Path does not exist")

    ai_plays(arguments, word_bank, secret_bank)
