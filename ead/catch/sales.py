from time import time, localtime, strftime
from ebaysdk import trading

class sales:
    def __init__(self, appid, devid, certid, token):
        self.appid = appid
        self.devid = devid
        self.certid = certid
        self.token = token

    def auth(self):
        self.api = trading(domain='api.sandbox.ebay.com', appid=self.appid, devid=self.devid, certid=self.certid, token=self.token)
    def getOrder(self):
        begin = strftime("%Y-%m-%dT00:00:00.000Z", localtime(int(time())))
#        begin = "2014-06-09T00:00:00.000Z"
        now = strftime("%Y-%m-%dT%H:%M:%S.000Z", localtime(int(time())))
#        now = "2014-06-09T04:53:21.000Z"
        self.api.execute("GetOrders", {
            "ModTimeFrom": begin,
            "ModTimeTo": now,
            })

    def createList(self):
        orderData = self.api.response_dict()
        orderNum = 0
        orderList = {}
        orderList["orders"] = "0"
        orderList["order"] = []

        if orderData["OrderArray"].__len__() > 0:
            if orderData["OrderArray"]["Order"].__class__() == []:
                orderArray = []
                for order in orderData["OrderArray"]['Order']:
                    orderArray.append(order)
            else:
                orderArray = []
                orderArray.append(orderData["OrderArray"]['Order'])

            for order in orderArray:
                orderProperty = {}
                orderProperty["paid"] = order["AmountPaid"]["value"]
                orderProperty["shipprice"] = order["ShippingServiceSelected"]["ShippingServiceCost"]["value"]
                orderProperty["item"] = []
                itemNum = 0
    
                if order["TransactionArray"]["Transaction"].__class__() == []:
                    for item in order["TransactionArray"]["Transaction"]:
                        itemProperty = {}
                        itemProperty["itemid"] = item["Item"]["ItemID"]["value"]
                        itemProperty["price"] = item["TransactionPrice"]["value"]
                        orderProperty["item"].append(itemProperty)
                        itemNum += 1
                else:
                    itemProperty = {}
                    itemProperty["itemid"] = order["TransactionArray"]["Transaction"]["Item"]["ItemID"]["value"]
                    itemProperty["price"] = order["TransactionArray"]["Transaction"]["TransactionPrice"]["value"]
                    orderProperty["item"].append(itemProperty)
                    itemNum += 1
                orderProperty["items"] = str(itemNum)
                orderList["order"].append(orderProperty)
                orderNum += 1
            orderList["orders"] = str(orderNum)

        return orderList

