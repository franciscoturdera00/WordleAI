# WordleAI
[![codecov](https://codecov.io/gh/franciscoturdera00/WordleAI/branch/main/graph/badge.svg?token=hsoJlTJT0Q)](https://codecov.io/gh/franciscoturdera00/WordleAI)

An AI that plays a <a href="https://www.nytimes.com/games/wordle/index.html" target="_blank">Wordle</a>-like game.
Designed for variable-length words.

### Set Up
From the **root** directory:
<pre>
pip install -r requirements.txt
export PYTHONPATH=`pwd`
</pre>

### Usage
```
usage: wordle_ai.py [-h] STRATEGY ...

Wordle AI

optional arguments:
  -h, --help            show this help message and exit

positional arguments:
  STRATEGY
    random              Picks guesses at random

    simple_filter       Reduces sample size given the feedback from previous guess

    smart_guess         Chooses guess intelligently by finding frequency of letters 
                        to eliminate as many options as possible and reduces 
                        sample size given the feedback from guess

    index_decision      Chooses guess intelligently by finding frequency of letters at each
                        index of the word to eliminate as many options as possible and 
                        reduces sample size given the feedback from guess

    outside_the_box     Works just like index_decision, but also takes advantage of the 
                        secret bank and uses an explore/exploit approach to choose words 
                        from the word bank or a larger pool (secret bank) to eliminate more 
                        possible answers

    markov              Calculates the probability it will deliver the correct answer in the 
                        following guess and takes it into account when weighing each possible guess
```

### Strategies:
Once you pick a strategy, you will have the following arguments.
<pre>
usage: wordle_ai.py STRATEGY [-h] -w WORD [-wb WORD_BANK] [-a ATTEMPTS] [-p]

optional arguments:
  -h, --help            show this help message and exit

  -w WORD, --word WORD  Word to guess

  -wb WORD_BANK, --word-bank WORD_BANK
                        File Path for word bank to be used

  -a ATTEMPTS, --attempts ATTEMPTS
                        Attempts the AI receives

  -p, --print           Print progress of AI as it makes guesses
</pre>

By default, WordleAI uses the Official Wordle Word Bank, which some users may find limiting.
[More Word Banks are available for the user here](word_banks/).

If choosing the strategy ```outside_the_box```, you will also have the following optional argument at your disposal

```
  -sb SECRET_BANK, --secret-bank SECRET_BANK
                        File Path for auxiliary allowed guesses
```
By default, the secret bank will be empty.

# Performance

Runs AI Strategy a large number of times and find the average number of 
attempts it takes to find solution.

Performance testing is *very slow*. Strategies are run under a high number 
of iterations to ensure convergence.

### Usage
<pre>
performance.py [-h] [-s STRATEGY [STRATEGY ...]] [-u] [-p]
</pre>

Not adding any arguments will run all performance tests.
### Optional Arguments:
<pre>
  -h, --help                  show this help message and exit

  -s STRATEGY [STRATEGY ...], --strategy STRATEGY [STRATEGY ...]
                              strategies to test performance for

  -u, --update-analytics      store analytics gathered

  -p, --progress              shows progress of testing for each strategy tested
</pre>

### Performance Strategy Options:
<pre>
random_official           Random Strategy against the official Wordle word list

simple_filter_official    Simple Filter against the official Wordle word list

simple_filter_all_5       Simple Filter against a word bank with all 5 letter words

smart_guess_official      Smart Guess against the official Wordle word list

smart_guess_all_5         Smart Guess against a word bank with all 5 letter words

index_decision_official   Index Decision against the official Wordle word list

index_decision_all_5      Index Decision against a word bank with all 5 letter words

index_decision_large      Index Decision against a word bank against a simplified 5 letter words list

outside_the_box_official  Think Outside The Box against the official Wordle word list and Official Guess List

outside_the_box_large     Think Outside The Box against a simplified 5 letter words list and all 5 letters Guess List

markov_official           Markov against the official Wordle word list
</pre>

Current Performance Information can be found [here](performance_analytics/analytics.json).

# Manual Play
This program also offers a way for you to play!

### Usage: 
<pre>
manual_play.py [-h] [-a ATTEMPTS] [-wb WORD_BANK] [-sb SECRET_BANK]
</pre>

Optional Arguments:
<pre>
-h, --help                                    show this help message and exit

-a ATTEMPTS, --attempts ATTEMPTS              number of attempts the player receives

-wb WORD_BANK, --word-bank WORD_BANK          file path for Word Bank to be used for game

-sb SECRET_BANK, --secret-bank SECRET_BANK    file path for auxiliary allowed guesses
</pre>

By default, the Wordle official word bank and secret bank will be used. You can provide your own bank, or can use one provided [here](word_banks/).