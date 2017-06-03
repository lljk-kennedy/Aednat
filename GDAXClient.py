import GDAX
import json
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

class GDAXClient:

    json_indent = 3

    def __init__(self, product):
        self.product_id = product
        self.publicClient = GDAX.PublicClient(product_id=product)

    # https://docs.gdax.com/#get-products
    def getProducts(self):
        data = self.publicClient.getProducts()
        return json.dumps(data,indent=self.json_indent)

    # https://docs.gdax.com/#get-product-order-book
    def getProductOrderBook(self, level):
        data = self.publicClient.getProductOrderBook(level)
        return json.dumps(data, indent=self.json_indent)

    def getProductTicker(self):
        data = self.publicClient.getProductTicker()
        return json.dumps(data, indent=self.json_indent)

    def getProductTrades(self):
        data = self.publicClient.getProductTrades()
        return json.dumps(data, indent=self.json_indent)

    def getCurrentPrice(self):
        data = self.publicClient.getProductTicker()
        return json.dumps(float(data['ask']), indent=self.json_indent)

    def getProductHistoricRates(self):
        data = self.publicClient.getProductHistoricRates()
        return json.dumps(data, indent=self.json_indent)

    def getProduct24HrStats(self):
        data = self.publicClient.getProduct24HrStats()
        return json.dumps(data, indent=self.json_indent)

    def getCurrencies(self):
        data = self.publicClient.getCurrencies()
        return json.dumps(data, indent=self.json_indent)

    def getTime(self):
        data = self.publicClient.getTime()
        return json.dumps(data, indent=self.json_indent)

    def setProductId(self, product_id):
        self.product_id = product_id;
        self.publicClient = GDAX.PublicClient(product_id=self.product_id)


    def printBuys(self):
        data = self.publicClient.getProductOrderBook(level=2)

        objects = []
        performance = []
        total = 0

        for item in reversed(data['bids']):
            # print json.dumps(item, indent=self.json_indent)
            total = total + float(item[1])
            print "Bids @ " + item[0] + ": size " + item[1] + ", num-orders: ", item[2]
            objects.append(item[0])
            performance.append(total)

        y_pos = np.arange(len(objects))

        plt.bar(y_pos, performance, align='center', alpha=0.5)
        plt.xticks(y_pos,objects, rotation=90)
        plt.ylabel('Volume')
        plt.title('Buys')

        plt.show()

    def printAsks(self):
        data = self.publicClient.getProductOrderBook(level=2)


        objects = []
        performance = []
        total = 0

        for item in data['asks']:
            # print json.dumps(item, indent=self.json_indent)
            total = total + float(item[1])
            print "asks @ " + item[0] + ": size " + item[1] + ", num-orders: ", item[2]
            objects.append(item[0])
            performance.append(total)

        y_pos = np.arange(len(objects))

        plt.bar(y_pos, performance, align='center', alpha=0.5)
        plt.xticks(y_pos, objects, rotation=90)
        plt.ylabel('Volume')
        plt.title('Asks')

        plt.show()