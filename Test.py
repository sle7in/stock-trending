from iex import iex_stats
from iex import stock

aapl = stock("AAPL")

stats = iex_stats()
print(aapl.stats())

