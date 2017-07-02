import os
from GDAXClientWrapper import GDAXClientWrapper
import time
import sys
from termcolor import colored
import os

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

tradeDirection = str(sys.argv[1])
targetPrice = float(sys.argv[2])
productId = str(sys.argv[3])

client = GDAXClientWrapper(GDAXClientWrapper.ClientType['READ-ONLY'], environment=GDAXClientWrapper.Env["LIVE"], product=productId )

# The notifier function
def notify(title, subtitle, message):
    t = '-title {!r}'.format(title)
    s = '-subtitle {!r}'.format(subtitle)
    m = '-message {!r}'.format(message)
    os.system('terminal-notifier {}'.format(' '.join([m, t, s])))

# Calling the function

lastprice = 0.0
actualPrice = 0.0
thresholdWall = 5
thresholdMet = False

topHigh = 0
bottomLow = 0



color = "white"
trendColor = "white"
trendArrowUp = u'\u2b06'
trendArrowDown = u'\u2b07'
trendArrow = ""

lastMoveslist = list()

minMaxVal = 0


while True:

    lastprice = actualPrice
    actualPrice = float(client.getCurrentPrice())

    if minMaxVal == 0:
        minMaxVal = lastprice
        topHigh = lastprice
        bottomLow = lastprice

    if len(lastMoveslist) >= 5:
            lastMoveslist.pop(0)

    if tradeDirection == "sell":
        if actualPrice > lastprice:
            color = "green"
            trendColor = "green"
            trendArrow = trendArrowUp
            lastMoveslist.append(trendArrow)
        elif actualPrice == lastprice:
            color = "yellow"
        else:
            color = "red"
            trendColor = "red"
            trendArrow = trendArrowDown
            lastMoveslist.append(trendArrow)
    elif tradeDirection == "buy":
        if actualPrice > lastprice:
            color = "green"
            trendColor = "red"
            trendArrow = trendArrowUp
            lastMoveslist.append(trendArrow)
        elif actualPrice == lastprice:
            color = "yellow"
        else:
            color = "red"
            trendColor = "green"
            trendArrow = trendArrowDown
            lastMoveslist.append(trendArrow)

    if actualPrice > topHigh:
        topHigh = actualPrice
        notify(title = productId, subtitle = str(topHigh), message  = 'New High reached for ' + productId)

    if actualPrice < bottomLow:
        bottomLow = actualPrice
        notify(title = productId, subtitle = str(bottomLow), message  = 'New Low reached for ' + productId)

    if tradeDirection == "sell":
        if actualPrice > targetPrice:
            print colored("Actual: " + str(actualPrice) + " > Target: " + str(targetPrice) + "!!!", "blue")
            notify(title = productId, subtitle = tradeDirection, message  = 'Current price ' + str(actualPrice) + ' is greater than the target sell of' + str(targetPrice))
        else:
            print "[" + time.strftime('%a %H:%M:%S') + "] A: " + colored(str(actualPrice), color) + " < T: " + colored(str(targetPrice), "cyan") +  " | H: " + str(topHigh) + ", L: " + str(bottomLow)

    elif tradeDirection == "buy":
        if actualPrice < targetPrice:
            print colored("Actual: " + str(actualPrice) + " < Target: " + str(targetPrice) + "!!!", "blue")
            notify(title = productId, subtitle = tradeDirection, message  = 'Current price ' + str(actualPrice) + ' is less than the target sell of' + str(targetPrice))
        else:
            print "[" + time.strftime('%a %H:%M:%S') + "] A: " + colored(str(actualPrice), color) + " > T: " + colored(str(targetPrice), "cyan") +  " | H: " + str(topHigh) + ", L: " + str(bottomLow)


    time.sleep(1)
