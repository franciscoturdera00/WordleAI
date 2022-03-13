import argparse


def initiate_parser():
    parser = argparse.ArgumentParser(description='Wordle AI')
    parser.add_argument('-s', '--strategy', dest='strategy', nargs='?', default='simple_filter', const='simple_filter',
                        type=str, help='Strategy used in the game. Options include: random, simple_filter')
    parser.add_argument('-wb', '--wordbank', dest='word_bank', nargs='?', default="word_banks/wordle_official_list.txt",
                        const="word_banks/test.txt", type=str, help="File Path for word bank to be used")
    parser.add_argument('-w', '--word', dest='word', type=str, required=True, help='Word to guess')
    parser.add_argument('-a', '--attempts', dest='attempts', nargs='?', default=6, const=6, type=int,
                        help='Attempts the AI receives')
    parser.add_argument('-p', '--print', dest='print_mode', action='store_true', default=False,
                        help='Print progress of AI as it makes guesses')

    return parser.parse_args()
