from GDAXClientWrapper import GDAXClientWrapper

client = GDAXClientWrapper(GDAXClientWrapper.ClientType['FULL-ACCESS'], environment=GDAXClientWrapper.Env["TEST"], product="ETH-EUR" )


# publically accessible functions
client.getProducts()
# client.getProductTicker()
# client.getProductTrades()
# client.getProductHistoricRates()
# client.getProduct24HrStats()
# client.getCurrencies()
# client.getTime()

# requires auth
# client.getAccounts()
# client.getAccount("4271afec-d6c0-4f0f-af62-d5bfd3113eeb")
# client.getAccountHistory("4271afec-d6c0-4f0f-af62-d5bfd3113eeb")
# client.getAccountHolds("4271afec-d6c0-4f0f-af62-d5bfd3113eeb")
