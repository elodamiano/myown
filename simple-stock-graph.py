import yfinance as yf
import matplotlib.pyplot as plt


start_date = '2019-11-01'
end_date = '2022-07-05'

ticker = 'AAPL'

data = yf.download(ticker, start_date, end_date)

data.tail()

data['Adj Close'].plot()
plt.show()
