from GDAXClientWrapper import GDAXClientWrapper
import time
client = GDAXClientWrapper(GDAXClientWrapper.ClientType['FULL-ACCESS'], environment=GDAXClientWrapper.Env["LIVE"], product="ETH-EUR" )
# wsClient = GDAXClientWrapper(GDAXClientWrapper.ClientType['FEED'], environment=GDAXClientWrapper.Env["FEED"], product="ETH-EUR" )
# order_book =  GDAXClientWrapper(GDAXClientWrapper.ClientType['ORDERBOOK'], environment=GDAXClientWrapper.Env["ORDERBOOK"], product="ETH-EUR" )

# publically accessible functions
# client.getProducts()
# client.getProductTicker()
# client.getProductTrades()
# client.getProductHistoricRates()
# client.getProduct24HrStats()
# client.getCurrencies()
# client.getTime()

# requires auth
# client.getAccounts()
# testAccountID = "0ec2697b-ef2f-49eb-a486-4eb31ef323a5"
liveAccountID = "4271afec-d6c0-4f0f-af62-d5bfd3113eeb"
client.getAccount(liveAccountID)
# client.getAccountHistory(liveAccountID)
# client.getAccountHolds(testAccountID)

# Buy 0.01 BTC @ 100 USD
# buyParams = {
#         'price': '100.00', #USD
#         'size': '0.01', #BTC
#         'product_id': 'BTC-USD'
# }
# client.buy(buyParams)

# Sell 0.01 BTC @ 200 USD
sellParams = {
        'price': '198.00', #USD
        'size': '0.015', #BTC
        'product_id': 'ETH-EUR'
}
client.sell(sellParams)
client.getAccount(liveAccountID)

# client.cancelOrder("d50ec984-77a8-460a-b958-66f114b0de9b")
# client.cancelOrder(productId='BTC-USD')

# client.getOrders()
# client.getOrder("d50ec984-77a8-460a-b958-66f114b0de9b")
# client.getFills(product="ETH-BTC")

# Deposit into GDAX from Coinbase Wallet
# depositParams = {
#         'amount': '25.00', # Currency determined by account specified
#         'coinbase_account_id': '63e7ce02-aa4f-4ee0-b305-13902cde570c'
#
# }
# client.deposit(depositParams)


# Withdraw from GDAX into Coinbase Wallet
# withdrawParams = {
#         'amount': '1.00', # Currency determined by account specified
#         'coinbase_account_id': '536a541fa9393bb3c7000023'
# }
# client.withdraw(withdrawParams)


# wsClient.start()
# time.sleep(30)
# wsClient.close()


# order_book.start()
# time.sleep(60)
# order_book.close()
