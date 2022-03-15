# WordleAI

An AI that plays a Wordle-like game. Designed for variable-length words.

### Requirements:
<pre>
python3
pip3
tqdm
</pre>

#### Get tqdm:
<pre>
pip3 install tqdm
</pre>

### Usage
<pre>
wordle_ai.py [-h] [-s STRATEGY] [-wb WORD_BANK] [-sb SECRET_BANK] -w WORD [-a ATTEMPTS] [-p]
</pre>

### Optional Arguments:
<pre>
  -h, --help                                   show this help message and exit

  -s STRATEGY, --strategy STRATEGY             Strategy used in the game. Default: smart_guess

  -wb WORD_BANK, --word-bank WORD_BANK         File Path for word bank to be used

  -sb SECRET_BANK, --secret-bank SECRET_BANK   File Path to additional word list that may be used for guessing

  -w WORD, --word WORD                         Word to guess

  -a ATTEMPTS, --attempts ATTEMPTS             Attempts the AI receives

  -p, --print                                  Print progress of AI as it makes guesses
</pre>

### Strategies:
<pre>
random            Picks guesses at random

simple_filter     Reduces sample size given the feedback from previous guess

smart_guess       Chooses guess intelligently by finding frequency of letters to eliminate as
                  many options as possible and reduces sample size given the feedback from guess

index_decision    Chooses guess intelligently by finding frequency of letters at each index of
                  the word to eliminate as many options as possible and reduces sample size
                  given the feedback from guess
</pre>

There are various [word banks](word_banks/) available for user.

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
                              Strategies to test performance for

  -u, --update-analytics      Store analytics gathered

  -p, --progress              Shows progress of testing for each strategy tested
</pre>

### Performance Strategy Options:
<pre>
simple_filter_official    Simple Filter against the official Wordle word list

simple_filter_all_5       Simple Filter against a word bank with all 5 letter words

smart_guess_official      Smart Guess against the official Wordle word list

smart_guess_all_5         Smart Guess against a word bank with all 5 letter words

index_decision_official   Index Decision against the official Wordle word list

index_decision_all_5      Index Decision against a word bank with all 5 letter words
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

-a ATTEMPTS, --attempts ATTEMPTS              Number of attempts the player receives

-wb WORD_BANK, --word-bank WORD_BANK          Word Bank to be used for game

-sb SECRET_BANK, --secret-bank SECRET_BANK    File Path to additional word list that may be used for guessing
</pre>
