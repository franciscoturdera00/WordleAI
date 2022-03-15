import argparse


def initiate_parser():
    parser = argparse.ArgumentParser(description='Wordle AI')
    parser.add_argument('-s', '--strategy', dest='strategy', default='smart_guess', type=str,
                        help='Strategy used in the game. Options include: random, simple_filter, smart_guess,'
                             'index_decision')
    parser.add_argument('-wb', '--wordbank', dest='word_bank', default="word_banks/wordle_official_list.txt",
                        type=str, help="File Path for word bank to be used")
    parser.add_argument('-w', '--word', dest='word', type=str, required=True, help='Word to guess')
    parser.add_argument('-a', '--attempts', dest='attempts', default=6, type=int,
                        help='Attempts the AI receives')
    parser.add_argument('-p', '--print', dest='print_mode', action='store_true', default=False,
                        help='Print progress of AI as it makes guesses')

    return parser.parse_args()
