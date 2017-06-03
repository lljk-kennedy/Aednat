from GDAXClient import GDAXClient


# publicClient = GDAX.PublicClient()
# Set a default product
client = GDAXClient(product="ETH-EUR")


print client.getProductTicker()
client.printBuys()
client.printAsks()
# print getProductOrderBook(level=2)
# print getProductTrades()
# print getCurrentPrice()
# print getProductHistoricRates()

# print getProduct24HrStats()
# print getCurrencies()
# print getTime()
# printBuys()
# printAsks()
