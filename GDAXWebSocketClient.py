import GDAX, time


class myWebsocketClient(GDAX.WebsocketClient):

    def on_open(self):
        self.url = "wss://ws-feed.gdax.com/"
        self.products = ["ETH-USD"]
        self.message_count = 0
        print("Lets count the messages!")

    def on_message(self, msg):
        self.message_count += 1
        if 'price' in msg and 'type' in msg:
            print ("Message type:", msg["type"], 
                   "\t@ {}.3f".format(float(msg["price"])))
    def on_close(self):
        print("-- Goodbye! --")

wsClient = myWebsocketClient()
wsClient.start()

print(wsClient.url, wsClient.products)

wsClient.close()