from config.arguments_parser import initiate_parser
from game_logic.ai_play import play_ai


def ai_plays(args):
    win, attempts = play_ai(args.strategy.lower(), word_bank, args.word.lower(), args.attempts, args.print_mode)
    if win:
        print("Win in %d attempts! Word: %s" % (attempts, args.word))
    else:
        print("Lose :( Word: %s" % args.word)


if __name__ == '__main__':
    arguments = initiate_parser()
    with open(arguments.word_bank) as f:
        word_bank = [x.replace("\n", "").lower() for x in f.readlines()]
    word_bank = set(word_bank)
    # Manual play in development
    ai_plays(arguments)
