import argparse


def performance_parser():
    parser = argparse.ArgumentParser(description='Performance Testing')
    parser.add_argument('-s', '--strategy', nargs='*', dest='strategy', type=str, default=None, const=None,
                        help='Strategy to test performance for')
    parser.add_argument('-u', '--update-analytics', dest='update_analytics', action='store_true', default=False,
                        help='Store analytics gathered')
    return parser.parse_args()
