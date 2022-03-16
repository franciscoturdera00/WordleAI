import argparse


def initiate_parser():
    parser = argparse.ArgumentParser(description='Wordle AI')
    parser.add_argument('-w', '--word', dest='word', type=str, required=True, help='Word to guess')
    parser.add_argument('-s', '--strategy', dest='strategy', default='index_decision', type=str,
                        help='Strategy used in the game. Options include: random, simple_filter, smart_guess,'
                             'index_decision, outside_the_box')
    parser.add_argument('-wb', '--word-bank', dest='word_bank', default="word_banks/wordle_official_list.txt",
                        type=str, help="File Path for word bank to be used")
    parser.add_argument('-sb', '--secret-bank', dest='secret_bank', default=None,
                        type=str, help="File Path for auxiliary allowed guesses")
    parser.add_argument('-a', '--attempts', dest='attempts', default=6, type=int,
                        help='Attempts the AI receives')
    parser.add_argument('-p', '--print', dest='print_mode', action='store_true', default=False,
                        help='Print progress of AI as it makes guesses')

    return parser.parse_args()
