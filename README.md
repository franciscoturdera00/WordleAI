# WordleAI

An AI that plays a Wordle-like game.

### Requirements:
<pre>Python3</pre>

### Usage
<pre>
wordle_ai.py [-h] [-s [STRATEGY]] [-wb [WORD_BANK]] -w WORD [-a [ATTEMPTS]] [-p]
</pre>

### optional arguments:
<pre>
-h, --help                                 show this help message and exit

-s [STRATEGY], --strategy [STRATEGY]       Strategy used in the game. Options include: random, simple_filter

-wb [WORD_BANK], --wordbank [WORD_BANK]    File Path for word bank to be used

-w WORD, --word WORD                       Word to guess

-a [ATTEMPTS], --attempts [ATTEMPTS]       Attempts the AI receives

-p, --print                                Print progress of AI as it makes guesses
</pre>

There are various [word banks](word_banks/) available for user.