import argparse

from config.ai_cli_hander import (
    play_index_decision,
    play_markov,
    play_outside_the_box,
    play_random,
    play_simple_filter,
    play_smart_guess,
)


def initiate_parser():
    parser = argparse.ArgumentParser(description="Wordle AI")

    parent_parser = argparse.ArgumentParser(add_help=False)
    parent_parser.add_argument("-w", "--word", dest="word", type=str, required=True, help="Word to guess")
    parent_parser.add_argument(
        "-wb",
        "--word-bank",
        dest="word_bank",
        default="word_banks/wordle_official_list.txt",
        type=str,
        help="File Path for word bank to be used",
    )
    parent_parser.add_argument(
        "-a", "--attempts", dest="attempts", default=6, type=int, help="Attempts the AI receives"
    )
    parent_parser.add_argument(
        "-p",
        "--print",
        dest="print_mode",
        action="store_true",
        default=False,
        help="Print progress of AI as it makes guesses",
    )

    advanced_parent = argparse.ArgumentParser(add_help=False, parents=[parent_parser])
    advanced_parent.add_argument(
        "-sb",
        "--secret-bank",
        dest="secret_bank",
        default=None,
        type=str,
        help="File Path for auxiliary allowed guesses",
    )

    subparsers = parser.add_subparsers(metavar="STRATEGY", required=True)

    rand = subparsers.add_parser("random", parents=[parent_parser], help="Picks guesses at random")
    rand.set_defaults(func=play_random)

    sf = subparsers.add_parser(
        "simple_filter", parents=[parent_parser], help="Reduces sample size given the feedback from previous guess"
    )
    sf.set_defaults(func=play_simple_filter)

    sg = subparsers.add_parser(
        "smart_guess",
        parents=[parent_parser],
        help="Chooses guess intelligently by finding frequency of letters to eliminate as many options as possible \
            and reduces sample size given the feedback from guess",
    )
    sg.set_defaults(func=play_smart_guess)

    id = subparsers.add_parser(
        "index_decision",
        parents=[parent_parser],
        help="Chooses guess intelligently by finding frequency of letters at each index of the word to eliminate as \
            many options as possible and reduces sample size given the feedback from guess",
    )
    id.set_defaults(func=play_index_decision)

    otb = subparsers.add_parser(
        "outside_the_box",
        parents=[advanced_parent],
        help="Works just like index_decision, but also \
         takes advantage of the secret bank and uses an explore/exploit approach to choose words from the word bank \
             or a larger pool (secret bank) to eliminate more possible answers",
    )
    otb.set_defaults(func=play_outside_the_box)

    mark = subparsers.add_parser(
        "markov",
        parents=[parent_parser],
        help="Calculates the probability it will deliver the \
         correct answer in the following guess  and takes it into account when weighing each possible guess",
    )
    mark.set_defaults(func=play_markov)

    return parser.parse_args()
