from game_logic.ai_play import game
from strategies.index_decision import IndexDecisionStrategy
from strategies.markov import MarkovStrategy
from strategies.outside_the_box import ThinkOutsideTheBoxStrategy
from strategies.random_strategy import RandomStrategy
from strategies.simple_filter import SimpleFilterStrategy
from strategies.smart_guess import SmartGuessStrategy


def play_random(args):
    wb = get_word_list(args.word_bank)
    strat = RandomStrategy(wb, set(), len(args.word), args.attempts)
    game(strat, wb.copy(), set(), args.word, args.attempts, args.print_mode)
    exit()


def play_simple_filter(args):
    wb = get_word_list(args.word_bank)
    strat = SimpleFilterStrategy(wb, set(), len(args.word), args.attempts)
    game(strat, wb.copy(), set(), args.word, args.attempts, args.print_mode)
    exit()


def play_smart_guess(args):
    wb = get_word_list(args.word_bank)
    strat = SmartGuessStrategy(wb, set(), len(args.word), args.attempts)
    game(strat, wb.copy(), set(), args.word, args.attempts, args.print_mode)
    exit()


def play_index_decision(args):
    wb = get_word_list(args.word_bank)
    strat = IndexDecisionStrategy(wb, set(), len(args.word), args.attempts)
    game(strat, wb.copy(), set(), args.word, args.attempts, args.print_mode)
    exit()


def play_outside_the_box(args):
    wb = get_word_list(args.word_bank)
    sb = get_secret_list(args.secret_bank)
    strat = ThinkOutsideTheBoxStrategy(wb, sb, len(args.word), args.attempts)
    game(strat, wb.copy(), sb.copy(), args.word, args.attempts, args.print_mode)
    exit()


def play_markov(args):
    wb = get_word_list(args.word_bank)
    strat = MarkovStrategy(wb, set(), len(args.word), args.attempts)
    game(strat, wb.copy(), set(), args.word, args.attempts, args.print_mode)
    exit()


def get_word_list(words_path):
    try:
        with open(words_path) as f:
            word_bank = set([x.replace("\n", "").lower() for x in f.readlines()])
    except OSError as e:
        exit(str(e))
    return word_bank


def get_secret_list(secret_path):
    secret_bank = set()
    try:
        if secret_path is not None:
            with open(secret_path) as g:
                secret_bank = set([x.replace("\n", "").lower() for x in g.readlines()])
    except OSError as e:
        exit(str(e))
    return secret_bank
