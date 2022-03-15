from strategies.feedback import Feedback
from util.constants import LIST_OF_LETTERS
from util.functions import flatten


def analyze_guess(guess, answer, *wordbanks):
    """Returns information of the guess in relation to the correct answer"""
    if len(guess) != len(answer):
        raise ValueError("Word Bank or Word contains wrong length words")
    all_words = set(flatten(wordbanks))
    if guess not in all_words:
        raise ValueError("Guess '%s' not in dictionary or already used" % guess)
    feedback = [Feedback.NOT_IN_WORD] * len(answer)
    correct_found = dict.fromkeys(LIST_OF_LETTERS, 0)
    letter_found = dict.fromkeys(LIST_OF_LETTERS, 0)
    for i, c in enumerate(answer):
        if guess[i] == c:
            feedback[i] = Feedback.CORRECT
            correct_found[c] += 1
    for i, c in enumerate(answer):
        if guess[i] == c:
            continue
        if guess[i] in answer and correct_found[guess[i]] + letter_found[guess[i]] < answer.count(guess[i]):
            feedback[i] = Feedback.IN_WORD
            letter_found[guess[i]] += 1
    return feedback
