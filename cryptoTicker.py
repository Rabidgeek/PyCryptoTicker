import shrimpy
import plotly.graph_objects as go

public_key = '510a439a466904076cf439307ecf6f53806df78d49c210bac06e83746be2daf4'
secret_key = '103fb3901b000916f351e0551efbc947baab6fa5f34204459fe0ae74a6d67f5e4e9b5e2319b03f33b57f931fb3aa7331a6de8e14e613f4e4ae11db9175488204'

client = shrimpy.ShrimpyApiClient(public_key, secret_key)

candles = client.get_candles(
	'binance', 	# exchange
	'XLM', 		# base_trading_symbol
	'BTC', 		# quote_trading_symbol
	'15m'		#interval
)

dates = []
open_data = []
high_data = []
low_data = []
close_data = []

for candle in candles:
	dates.append(candle['time'])
	open_data.append(candle['open'])
	high_data.append(candle['high'])
	low_data.append(candle['low'])
	close_data.append(candle['close'])

fig = go.Figure(data = [go.Candlestick(x = dates, open = open_data, high = high_data, low = low_data, close = close_data)])

fig.show()


