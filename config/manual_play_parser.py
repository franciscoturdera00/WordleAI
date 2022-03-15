import argparse


def manual_parser():
    parser = argparse.ArgumentParser(description='Play Wordle')
    parser.add_argument('-a', '--attempts', dest='attempts', default=6, help='Number of attempts the player receives')
    parser.add_argument('-wb', '--wordbank', dest='word_bank', default=None, help='Word Bank to be used for game')

    return parser.parse_args()
