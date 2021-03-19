#Setting up Shrimpy websocket to retrieve crypto prices
#importing Shrimpy
import shrimpy

#error handler
def error_handler(err):
	print(err)

#handler for output stream
def handler(msg):
	ticker = msg['content'][len(msg['content'])-1]['price']
	print(ticker)

#Shrimpy API Keys
public_key = '510a439a466904076cf439307ecf6f53806df78d49c210bac06e83746be2daf4'
private_key = '103fb3901b000916f351e0551efbc947baab6fa5f34204459fe0ae74a6d67f5e4e9b5e2319b03f33b57f931fb3aa7331a6de8e14e613f4e4ae11db9175488204'

#Shrimpy websocket client
def btcWS():
	api_client = shrimpy.ShrimpyApiClient(public_key, private_key)
	raw_token = api_client.get_token()
	client = shrimpy.ShrimpyWsClient(error_handler, raw_token['token'])

	#Subscription object
	subscribe_data = {
		"type": "subscribe",
		"exchange": "binance", 
		"pair": "btc-usdt",
		"channel": "trade"
	}

	client.connect()
	client.subscribe(subscribe_data, handler)

#Setting up the GUI
#importing App from guizero 
from guizero import App, Text

#Setting up the workspace
app = App(title = "G33k's Cryptocurrency Ticker", width = 600, height = 400)
app.bg = "white"

test = "test"
#Print the cryptocurrencies to be displayed
btc = Text(app, text = "Bitcoin (BTC):				$", size = 24, align = 'left')
btcValue = Text(app, text = "0",size = 24, align = 'right')
btcValue.after(1000, btcWS)
#bch = Text(app, text = "Bitcoin Cash (BCH)		$", size = 24, align = 'left')
#eth = Text(app, text = "Ethereum (ETH):		$", size = 24, align = 'left')
#xlm = Text(app, text = "Stellar (XLM):		$", size = 24, align = 'left')
#xrp = Text(app, text = "Ripple (XRP):		$", size = 24, align = 'left')
#dog = Text(app, text = "Dogecoin (DOGE):		$", size = 24, align = 'left')


app.display()