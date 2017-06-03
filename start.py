from GDAXClient import GDAXClient


# publicClient = GDAX.PublicClient()
# Set a default product
client = GDAXClient(product="ETH-EUR")

client.getProducts()
client.getProductTicker()
client.getProductTrades()
client.getProductHistoricRates()
client.getProduct24HrStats()
client.getCurrencies()
client.getTime()
