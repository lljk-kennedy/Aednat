import GDAX
import json
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import logging
import datetime
import configparser
from enum import Enum

logging.basicConfig(filename='output.log',level=logging.DEBUG)

class GDAXClientWrapper:

    json_indent = 3
    ClientType = Enum('ClientType', 'PUBLIC READ-ONLY READ-TRANSFER READ-TRANSFER-TRADE FULL-ACCESS')

    def __init__(self, client_type, product):
        self.product_id = product
        config = configparser.ConfigParser()
        config.read('apiKeys.config')

        if client_type == self.ClientType['PUBLIC']:
            self.publicClient = GDAX.PublicClient(product_id=product)
            self.authType = "PUBLIC (** NO AUTH **)"
        elif client_type == self.ClientType['READ-ONLY']:
            self.publicClient = GDAX.AuthenticatedClient(config['READ-ONLY']['key'], config['READ-ONLY']['b64secret'], config['READ-ONLY']['passphrase'], product_id=product)
            self.authType = "READ-ONLY (" + config['READ-ONLY']['key'] + ")"
        elif client_type == self.ClientType['READ-TRANSFER']:
            self.publicClient = GDAX.AuthenticatedClient(config['READ-TRANSFER']['key'], config['READ-TRANSFER']['b64secret'], config['READ-TRANSFER']['passphrase'], product_id=product)
            self.authType = "READ-TRANSFER (" + config['READ-TRANSFER']['key'] + ")"
        elif client_type == self.ClientType['READ-TRANSFER-TRADE']:
            self.publicClient = GDAX.AuthenticatedClient(config['READ-TRANSFER-TRADE']['key'], config['READ-TRANSFER-TRADE']['b64secret'], config['READ-TRANSFER-TRADE']['passphrase'], product_id=product)
            self.authType = "READ-TRANSFER-TRADE (" + config['READ-TRANSFER-TRADE']['key'] + ")"
        elif client_type == self.ClientType['FULL-ACCESS']:
            self.publicClient = GDAX.AuthenticatedClient(config['FULL-ACCESS']['key'], config['FULL-ACCESS']['b64secret'], config['FULL-ACCESS']['passphrase'], product_id=product)
            self.authType = "FULL-ACCESS (" + config['FULL-ACCESS']['key'] + ")"

        logging.info("*** [" + self.authType + "] CLIENT: authenticated at " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " ******")


    # https://docs.gdax.com/#get-products
    def getProducts(self):
        data = self.publicClient.getProducts()
        logging.info("*** [" + self.authType + "] CLIENT: getProducts called at " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " ******")
        retVal = json.dumps(data,indent=self.json_indent)
        logging.info(retVal)
        return retVal

    # https://docs.gdax.com/#get-product-order-book
    def getProductOrderBook(self, level):
        data = self.publicClient.getProductOrderBook(level)
        logging.info("*** [" + self.authType + "] CLIENT: getProductOrderBook called at " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " ******")
        retVal = json.dumps(data,indent=self.json_indent)
        logging.info(retVal)
        return retVal

    def getProductTicker(self):
        data = self.publicClient.getProductTicker()
        logging.info("*** [" + self.authType + "] CLIENT: getProductTicker called at " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " ******")
        retVal = json.dumps(data,indent=self.json_indent)
        logging.info(retVal)
        return retVal

    def getProductTrades(self):
        data = self.publicClient.getProductTrades()
        logging.info("*** [" + self.authType + "] CLIENT: getProductTrades called at " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " ******")
        retVal = json.dumps(data,indent=self.json_indent)
        logging.info(retVal)
        return retVal

    def getCurrentPrice(self):
        data = self.publicClient.getProductTicker()
        logging.info("*** [" + self.authType + "] CLIENT: getCurrentPrice called at " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " ******")
        retVal = json.dumps(float(data['ask']), indent=self.json_indent)
        logging.info(retVal)
        return retVal

    def getProductHistoricRates(self):
        data = self.publicClient.getProductHistoricRates()
        logging.info("*** [" + self.authType + "] CLIENT: getProductHistoricRates called at " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " ******")
        retVal = json.dumps(data,indent=self.json_indent)
        logging.info(retVal)
        return retVal

    def getProduct24HrStats(self):
        data = self.publicClient.getProduct24HrStats()
        logging.info("*** [" + self.authType + "] CLIENT: getProduct24HrStats called at " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " ******")
        retVal = json.dumps(data,indent=self.json_indent)
        logging.info(retVal)
        return retVal

    def getCurrencies(self):
        data = self.publicClient.getCurrencies()
        logging.info("*** [" + self.authType + "] CLIENT: getCurrencies called at " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " ******")
        retVal = json.dumps(data,indent=self.json_indent)
        logging.info(retVal)
        return retVal

    def getTime(self):
        data = self.publicClient.getTime()
        logging.info("*** [" + self.authType + "] CLIENT: getTime called at " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " ******")
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
