# WordleAI

An AI that plays a Wordle-like game.

### Requirements:
<pre>Python3</pre>

### Usage
<pre>
wordle_ai.py [-h] [-s STRATEGY] [-wb WORD_BANK] -w WORD [-a ATTEMPTS] [-p]
</pre>

### Optional Arguments:
<pre>
  -h, --help                            show this help message and exit

  -s STRATEGY, --strategy STRATEGY      Strategy used in the game

  -wb WORD_BANK, --wordbank WORD_BANK   File Path for word bank to be used

  -w WORD, --word WORD                  Word to guess

  -a ATTEMPTS, --attempts ATTEMPTS      Attempts the AI receives

  -p, --print                           Print progress of AI as it makes guesses
</pre>

### Strategies:
<pre>
random: Picks guesses at random

simple_filter: Reduces sample size given the feedback from previous guess

smart_guess: chooses guess intelligently by finding frequency of letters to eliminate as many options as possible
and reduces sample size given the feedback from guess
</pre>

There are various [word banks](word_banks/) available for user.

# Performance:
### Usage
<pre>
performance.py [-h] [-s STRATEGY]
</pre>
### Optional Arguments:
<pre>
  -h, --help                         show this help message and exit
  -s STRATEGY, --strategy STRATEGY   Strategy to test performance for
</pre>

### Performance Strategy Options:
<pre>
simple_filter_official: Simple Filter against the official Wordle word list

simple_filter_all_5: Simple Filter against a word bank with all 5 letter words

smart_guess_official: Smart Guess against the official Wordle word list

smart_guess_all_5: Smart Guess against a word bank with all 5 letter words
</pre>