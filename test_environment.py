from strategies.random_strategy import RandomStrategy

strat = RandomStrategy("word_banks/test.txt", 5)
print(strat.guess())
print(strat.guess())
print(strat.guess())
print(strat.guess())