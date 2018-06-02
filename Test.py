from iex import iex_stats
from iex import stock

aapl = stock("AAPL")

stats = iex_stats()
intraday = iex_stats(date_format='datetime').intraday()
print(aapl.stats())


