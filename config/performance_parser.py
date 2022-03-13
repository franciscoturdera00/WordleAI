import argparse


def performance_parser():
    parser = argparse.ArgumentParser(description='Performance Testing')
    parser.add_argument('-s', '--strategy', dest='strategy', type=str, help='Strategy to test performance for')
    return parser.parse_args()
