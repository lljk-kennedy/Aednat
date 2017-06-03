import GDAX
import json
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import logging
import datetime

logging.basicConfig(filename='output.log',level=logging.INFO)

class GDAXClient:

    json_indent = 3

    def __init__(self, product):
        self.product_id = product
        self.publicClient = GDAX.PublicClient(product_id=product)

    # https://docs.gdax.com/#get-products
    def getProducts(self):
        data = self.publicClient.getProducts()
        logging.info("*** getProducts called at " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " ******")
        retVal = json.dumps(data,indent=self.json_indent)
        logging.info(retVal)
        return retVal

    # https://docs.gdax.com/#get-product-order-book
    def getProductOrderBook(self, level):
        data = self.publicClient.getProductOrderBook(level)
        logging.info("*** getProductOrderBook called at " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " ******")
        retVal = json.dumps(data,indent=self.json_indent)
        logging.info(retVal)
        return retVal

    def getProductTicker(self):
        data = self.publicClient.getProductTicker()
        logging.info("*** getProductTicker called at " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " ******")
        retVal = json.dumps(data,indent=self.json_indent)
        logging.info(retVal)
        return retVal

    def getProductTrades(self):
        data = self.publicClient.getProductTrades()
        logging.info("*** getProductTrades called at " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " ******")
        retVal = json.dumps(data,indent=self.json_indent)
        logging.info(retVal)
        return retVal

    def getCurrentPrice(self):
        data = self.publicClient.getProductTicker()
        logging.info("*** getCurrentPrice called at " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " ******")
        retVal = json.dumps(float(data['ask']), indent=self.json_indent)
        logging.info(retVal)
        return retVal

    def getProductHistoricRates(self):
        data = self.publicClient.getProductHistoricRates()
        logging.info("*** getProductHistoricRates called at " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " ******")
        retVal = json.dumps(data,indent=self.json_indent)
        logging.info(retVal)
        return retVal

    def getProduct24HrStats(self):
        data = self.publicClient.getProduct24HrStats()
        logging.info("*** getProduct24HrStats called at " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " ******")
        retVal = json.dumps(data,indent=self.json_indent)
        logging.info(retVal)
        return retVal

    def getCurrencies(self):
        data = self.publicClient.getCurrencies()
        logging.info("*** getCurrencies called at " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " ******")
        retVal = json.dumps(data,indent=self.json_indent)
        logging.info(retVal)
        return retVal

    def getTime(self):
        data = self.publicClient.getTime()
        logging.info("*** getTime called at " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " ******")
        retVal = json.dumps(data,indent=self.json_indent)
        logging.info(retVal)
        return retVal

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
