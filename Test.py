"""
    o- Using python wrapper alpha_vantage:
        https://github.com/RomelTorres/alpha_vantage
        API key for https://www.alphavantage.co/documentation/: YTXURN2UGYWTAWXI
    - Using iexfinance as IEX Python wrapper:
        https://pypi.org/project/iexfinance/
    - Using macrotrends for key indicator tracking
        http://www.macrotrends.net/stocks/charts/AAPL/debt-equity-ratio/apple-inc-debt-equity-ratio-history
    x- Using iex as IEX Python wrapper:
        https://libraries.io/pypi/iex-api-python

"""

#===================== alpha_vantage wrapper for AlphaVantage ====================
## example using alpha_vantage python api wrapper for alphaVantage stock data calls
# from alpha_vantage.timeseries import TimeSeries
# ts = TimeSeries(key='YTXURN2UGYWTAWXI', output_format='pandas')
# # Get json object with the intraday data and another with  the call's metadata
# data, meta_data = ts.get_intraday('GOOGL') 
# print(data.head())

# from alpha_vantage.timeseries import TimeSeries
# import matplotlib.pyplot as plt

# ts = TimeSeries(key='YOUR_API_KEY', output_format='pandas')
# data, meta_data = ts.get_intraday(symbol='MSFT',interval='1min', outputsize='full')
# data['4. close'].plot()
# plt.title('Intraday Times Series for the MSFT stock (1 min)')
# plt.show()



#======================= iexfinance wrapper for IEX ===============================
# from iexfinance import get_market_tops, get_stats_intraday
# ## get_market_tops() is a lib top level function, instantiating TOPS;
# ## get_stats_intraday instatiates IntradayReader for IEX market meta data
# print(get_stats_intraday())
# ## only seems to return during market hours
# for i, stock in enumerate(get_market_tops()):
#     if stock['symbol'] == 'AAPL':
#         print(i, stock)



#======================= iex wrapper for IEX ======================================
# from iex import stock, market, iex_stats

# aapl = stock("AAPL")
# # print(aapl.earnings())
# # print(aapl.stats())

# m = market()
# # print(m.gainers())
# # print(m.news())

# # print(stock("F").chart_table(range="1y").head())


# ## returns Exchange data, unapplicable to general stocks
# from iex import iex_stats
# stats = iex_stats(date_format='datetime')
# print stats.intraday()
# print(stats.historical_summary('201804'))





