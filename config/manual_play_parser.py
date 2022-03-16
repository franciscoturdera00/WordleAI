import argparse


def manual_parser():
    parser = argparse.ArgumentParser(description='Play Wordle')
    parser.add_argument('-a', '--attempts', dest='attempts', default=6, help='Number of attempts the player receives')
    parser.add_argument('-wb', '--word-bank', dest='word_bank', default=None, help='Word Bank to be used for game')
    parser.add_argument('-sb', '--secret-bank', dest='secret_bank', default=None,
                        help='File Path for auxiliary allowed guesses')
    return parser.parse_args()
