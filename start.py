from GDAXClient import GDAXClient


# publicClient = GDAX.PublicClient()
# Set a default product
client = GDAXClient(product="ETH-EUR")
print "****** getProducts ******"
print client.getProducts()

print "****** getProductTicker() ******"
print client.getProductTicker()

print "****** getProductTrades() ******"
print client.getProductTrades()

print "****** getProductHistoricRates() ******"
print client.getProductHistoricRates()

print "****** getProduct24HrStats() ******"
print client.getProduct24HrStats()

print "****** getCurrencies() ******"
print client.getCurrencies()

print "****** getTime() ******"
print client.getTime()
