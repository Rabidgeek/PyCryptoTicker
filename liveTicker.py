import shrimpy

def error_handler(err):
	print(err)

def handler(msg):
	ticker = msg['content'][len(msg['content']) - 1]['price']
	print(ticker)

public_key = '510a439a466904076cf439307ecf6f53806df78d49c210bac06e83746be2daf4'
private_key = '103fb3901b000916f351e0551efbc947baab6fa5f34204459fe0ae74a6d67f5e4e9b5e2319b03f33b57f931fb3aa7331a6de8e14e613f4e4ae11db9175488204'

api_client = shrimpy.ShrimpyApiClient(public_key, private_key)
raw_token = api_client.get_token()
client = shrimpy.ShrimpyWsClient(error_handler, raw_token['token'])

subscribe_data = {
	"type": "subscribe",
	"exchange": "binance", 
	"pair": "btc-usdt",
	"channel": "trade"
}

client.connect()
client.subscribe(subscribe_data, handler)


client.disconnect()

