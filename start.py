from GDAXPublicClient import GDAXPublicClient
from GDAXClientWrapper import GDAXClientWrapper


client = GDAXClientWrapper(GDAXClientWrapper.ClientType['PUBLIC'], product="ETH-EUR" )

client.getProducts()
client.getProductTicker()
client.getProductTrades()
client.getProductHistoricRates()
client.getProduct24HrStats()
client.getCurrencies()
client.getTime()
