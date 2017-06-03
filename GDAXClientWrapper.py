import GDAX
import json
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import logging
import datetime
import configparser
from enum import Enum

logging.basicConfig(filename='./logs/'+datetime.datetime.now().strftime("%Y-%m-%d")+'.log',level=logging.DEBUG)

class GDAXClientWrapper:

    json_indent = 3
    ClientType = Enum('ClientType', 'PUBLIC READ-ONLY READ-TRANSFER READ-TRANSFER-TRADE FULL-ACCESS')
    Env = Enum('Env', 'TEST LIVE')

    def __init__(self, client_type, environment, product):
        self.product_id = product
        self.client_type = client_type
        self.environment_type = environment

        config = configparser.ConfigParser()
        config.read('./config/config.config')

        if self.client_type == self.ClientType['PUBLIC']:
            self.client = GDAX.PublicClient(product_id=product)
            self.clientTypeForLogging = "PUBLIC (** NO AUTH **)"

        elif self.client_type == self.ClientType['READ-ONLY']:
            self.client = GDAX.AuthenticatedClient( key=config['READ-ONLY-'+str(self.environment_type.name)]['key'],
                                                    b64secret=config['READ-ONLY-'+str(self.environment_type.name)]['b64secret'],
                                                    passphrase=config['READ-ONLY-'+str(str(self.environment_type.name))]['passphrase'],
                                                    api_url= config["API-ENDPOINT"][str(str(self.environment_type.name))],
                                                    product_id=product)
            self.clientTypeForLogging = "READ-ONLY (" + config['READ-ONLY-'+str(self.environment_type.name)]['key'] + ")"

        elif self.client_type == self.ClientType['READ-TRANSFER']:
            self.client = GDAX.AuthenticatedClient( key=config['READ-TRANSFER-'+str(self.environment_type.name)]['key'],
                                                    b64secret=config['READ-TRANSFER-'+str(self.environment_type.name)]['b64secret'],
                                                    passphrase=config['READ-TRANSFER-'+str(self.environment_type.name)]['passphrase'],
                                                    api_url= config["API-ENDPOINT"][(str(self.environment_type.name))],
                                                    product_id=product)
            self.clientTypeForLogging = "READ-TRANSFER (" + config['READ-TRANSFER-'+str(self.environment_type.name)]['key'] + ")"

        elif self.client_type == self.ClientType['READ-TRANSFER-TRADE']:
            self.client = GDAX.AuthenticatedClient( key=config['READ-TRANSFER-TRADE-'+str(self.environment_type.name)]['key'],
                                                    b64secret=config['READ-TRANSFER-TRADE-'+str(self.environment_type.name)]['b64secret'],
                                                    passphrase=config['READ-TRANSFER-TRADE-'+str(self.environment_type.name)]['passphrase'],
                                                    api_url= config["API-ENDPOINT"][(str(self.environment_type.name))],
                                                    product_id=product)
            self.clientTypeForLogging = "READ-TRANSFER-TRADE (" + config['READ-TRANSFER-TRADE-'+str(self.environment_type.name)]['key'] + ")"

        elif self.client_type == self.ClientType['FULL-ACCESS']:
            self.client = GDAX.AuthenticatedClient( key=config['FULL-ACCESS-'+str(self.environment_type.name)]['key'],
                                                    b64secret=config['FULL-ACCESS-'+str(self.environment_type.name)]['b64secret'],
                                                    passphrase=config['FULL-ACCESS-'+str(self.environment_type.name)]['passphrase'],
                                                    api_url= config["API-ENDPOINT"][(str(self.environment_type.name))],
                                                    product_id=product)
            self.clientTypeForLogging = "FULL-ACCESS (" + config['FULL-ACCESS-'+str(self.environment_type.name)]['key'] + ")"

        logging.info("ENV: " + str(self.environment_type.name) + " | *** [" + self.clientTypeForLogging + "] CLIENT: authenticated at " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " ******")


    # https://docs.gdax.com/#get-products
    def getProducts(self):
        try:
            data = self.client.getProducts()
            logging.info("ENV: " + str(self.environment_type.name) + " | [" + self.clientTypeForLogging + "] CLIENT: getProducts called at " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " ******")
            retVal = json.dumps(data,indent=self.json_indent)
            logging.info(retVal)
            return retVal
        except Exception as e:
            logging.error("ENV: " + str(self.environment_type.name) + " | [" + self.clientTypeForLogging + "] CLIENT: getProducts - " + str(e) + " ******")
            print e

    # https://docs.gdax.com/#get-product-order-book
    def getProductOrderBook(self, level):
        try:
            data = self.client.getProductOrderBook(level)
            logging.info("ENV: " + str(self.environment_type.name) + " | [" + self.clientTypeForLogging + "] CLIENT: getProductOrderBook called at " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " ******")
            retVal = json.dumps(data,indent=self.json_indent)
            logging.info(retVal)
            return retVal
        except Exception as e:
            logging.error("ENV: " + str(self.environment_type.name) + " | [" + self.clientTypeForLogging + "] CLIENT: getProductOrderBook - " + str(e) + " ******")
            print e

    def getProductTicker(self):
        try:
            data = self.client.getProductTicker()
            logging.info("ENV: " + str(self.environment_type.name) + " | [" + self.clientTypeForLogging + "] CLIENT: getProductTicker called at " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " ******")
            retVal = json.dumps(data,indent=self.json_indent)
            logging.info(retVal)
            return retVal
        except Exception as e:
            logging.error("ENV: " + str(self.environment_type.name) + " | [" + self.clientTypeForLogging + "] CLIENT: getProductTicker - " + str(e) + " ******")
            print e

    def getProductTrades(self):
        try:
            data = self.client.getProductTrades()
            logging.info("ENV: " + str(self.environment_type.name) + " | [" + self.clientTypeForLogging + "] CLIENT: getProductTrades called at " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " ******")
            retVal = json.dumps(data,indent=self.json_indent)
            logging.info(retVal)
            return retVal
        except Exception as e:
            logging.error("ENV: " + str(self.environment_type.name) + " | [" + self.clientTypeForLogging + "] CLIENT: getProductTrades - " + str(e) + " ******")
            print e

    def getCurrentPrice(self):
        try:
            data = self.client.getProductTicker()
            logging.info("ENV: " + str(self.environment_type.name) + " | [" + self.clientTypeForLogging + "] CLIENT: getCurrentPrice called at " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " ******")
            retVal = json.dumps(float(data['ask']), indent=self.json_indent)
            logging.info(retVal)
            return retVal
        except Exception as e:
            logging.error("ENV: " + str(self.environment_type.name) + " | [" + self.clientTypeForLogging + "] CLIENT: getCurrentPrices - " + str(e) + " ******")
            print e

    def getProductHistoricRates(self):
        data = self.client.getProductHistoricRates()
        logging.info("ENV: " + str(self.environment_type.name) + " | [" + self.clientTypeForLogging + "] CLIENT: getProductHistoricRates called at " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " ******")
        retVal = json.dumps(data,indent=self.json_indent)
        logging.info(retVal)
        return retVal

    def getProduct24HrStats(self):
        data = self.client.getProduct24HrStats()
        logging.info("ENV: " + str(self.environment_type.name) + " | [" + self.clientTypeForLogging + "] CLIENT: getProduct24HrStats called at " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " ******")
        retVal = json.dumps(data,indent=self.json_indent)
        logging.info(retVal)
        return retVal

    def getCurrencies(self):
        data = self.client.getCurrencies()
        logging.info("ENV: " + str(self.environment_type.name) + " | [" + self.clientTypeForLogging + "] CLIENT: getCurrencies called at " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " ******")
        retVal = json.dumps(data,indent=self.json_indent)
        logging.info(retVal)
        return retVal

    def getTime(self):
        data = self.client.getTime()
        logging.info("ENV: " + str(self.environment_type.name) + " | [" + self.clientTypeForLogging + "] CLIENT: getTime called at " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " ******")
        retVal = json.dumps(data,indent=self.json_indent)
        logging.info(retVal)
        return retVal

    def setProductId(self, product_id):
        self.product_id = product_id;
        self.client = GDAX.PublicClient(product_id=self.product_id)

    def printBuys(self):
        data = self.client.getProductOrderBook(level=2)

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

    def getAccounts(self):
        try:
            data = self.client.getAccounts()
            logging.info("ENV: " + str(self.environment_type.name) + " | [" + self.clientTypeForLogging + "] CLIENT: getAccounts called at " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " ******")
            retVal = json.dumps(data,indent=self.json_indent)
            logging.info(retVal)
            return retVal
        except Exception as e:
            logging.error("ENV: " + str(self.environment_type.name) + " | [" + self.clientTypeForLogging + "] CLIENT: getAccounts - " + str(e) + " ******")
            print e

    def getAccount(self, accountId):
        try:
            data = self.client.getAccount(accountId)
            logging.info("ENV: " + str(self.environment_type.name) + " | [" + self.clientTypeForLogging + "] CLIENT: getAccount called at " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " ******")
            retVal = json.dumps(data,indent=self.json_indent)
            logging.info(retVal)
            return retVal
        except Exception as e:
            logging.error("ENV: " + str(self.environment_type.name) + " | [" + self.clientTypeForLogging + "] CLIENT: getAccount - " + str(e) + " ******")
            print e

    def getAccountHistory(self, accountId):
        try:
            data = self.client.getAccountHistory(accountId)
            logging.info("ENV: " + str(self.environment_type.name) + " | [" + self.clientTypeForLogging + "] CLIENT: getAccountHistory called at " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " ******")
            retVal = json.dumps(data,indent=self.json_indent)
            logging.info(retVal)
            return retVal
        except Exception as e:
            logging.error("ENV: " + str(self.environment_type.name) + " | [" + self.clientTypeForLogging + "] CLIENT: getAccountHistory - " + str(e) + " ******")
            print e

    def getAccountHolds(self, accountId):
        try:
            data = self.client.getAccountHolds(accountId)
            logging.info("ENV: " + str(self.environment_type.name) + " | [" + self.clientTypeForLogging + "] CLIENT: getAccountHolds called at " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " ******")
            retVal = json.dumps(data,indent=self.json_indent)
            logging.info(retVal)
            return retVal
        except Exception as e:
            logging.error("ENV: " + str(self.environment_type.name) + " | [" + self.clientTypeForLogging + "] CLIENT: getAccountHolds - " + str(e) + " ******")
            print e


    def printAsks(self):
        data = self.client.getProductOrderBook(level=2)


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
