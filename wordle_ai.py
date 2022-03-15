from config.arguments_parser import initiate_parser
from game_logic.ai_play import play_ai
from util.functions import get_word_list_from


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
    word_bank = set()
    try:
        word_bank = get_word_list_from(arguments.word_bank)
    except OSError:
        exit("Word Bank Path does not exist")

    secret_bank = set()
    if arguments.secret_bank is not None:
        try:
            secret_bank = get_word_list_from(arguments.secret_bank)
        except OSError:
            exit("Secret Bank Path does not exist")

    ai_plays(arguments, word_bank, secret_bank)
