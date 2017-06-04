import os
from GDAXClientWrapper import GDAXClientWrapper
import time
import sys
from termcolor import colored

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

client = GDAXClientWrapper(GDAXClientWrapper.ClientType['READ-ONLY'], environment=GDAXClientWrapper.Env["LIVE"], product="ETH-EUR" )

# The notifier function
def notify(title, subtitle, message):
    t = '-title {!r}'.format(title)
    s = '-subtitle {!r}'.format(subtitle)
    m = '-message {!r}'.format(message)
    os.system('terminal-notifier {}'.format(' '.join([m, t, s])))

# Calling the function

lastprice = 0.0
actualPrice = 0.0

while True:
    sellPrice = float(sys.argv[1])
    lastprice = actualPrice
    actualPrice = client.getCurrentPrice()




    if actualPrice <= sellPrice:
        print colored("Actual price " + str(actualPrice) + " is less than the sell target of " + str(sellPrice) + "!!!", "blue")
        notify(title    = 'Ethereum', subtitle = '', message  = 'Current price ' + str(actualPrice) + ' is less than the target sell of' + str(sellPrice))
    else:
        if actualPrice > lastprice:
            print "Actual price " + colored(str(actualPrice), "green") + " is greater than sell target of " + colored(str(sellPrice), "cyan")
        elif actualPrice == lastprice:
            print "Actual price " + colored(str(actualPrice), "yellow") + " is greater than sell target of " + colored(str(sellPrice), "cyan")
        else:
            print "Actual price " + colored(str(actualPrice), "red") + " is greater than sell target of " + colored(str(sellPrice), "cyan")
    time.sleep(5)
