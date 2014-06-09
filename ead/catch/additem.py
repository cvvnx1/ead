from random import Random, uniform, randint
from ebaysdk import trading

class additem:
    def __init__(self, appid, devid, certid, token):
        self.appid = appid
        self.devid = devid
        self.certid = certid
        self.token = token
        self.name = ""

    def auth(self):
        self.api = trading(domain='api.sandbox.ebay.com', appid=self.appid, devid=self.devid, certid=self.certid, token=self.token)

    def add(self):
        self.name = "Book_%s" % self.randomStr()
        item = {"Item": {
            "Title": self.name,
            "Description": self.name + "_description",
            "PrimaryCategory": {"CategoryID": "377"},
            "StartPrice": "%.2f" % uniform(1, 50),
            "BuyItNowPrice": "%.2f" % uniform(51, 100),
            "ConditionID": "3000",
            "CategoryMappingAllowed": "true",
            "Country": "US",
            "Currency": "USD",
            "DispatchTimeMax": "3",
            "ListingDuration": "Days_10",
            "ListingType": "Chinese",
            "PaymentMethods": "PayPal",
            "PayPalEmailAddress": "cvvnx1@163.com",
            "PostalCode": "95125",
            "Quantity": "1",
            "ReturnPolicy": {"ReturnsAcceptedOption": "ReturnsAccepted", "RefundOption": "MoneyBack", "ReturnsWithinOption": "Days_30", "Description": "return the book for refund", "ShippingCostPaidByOption": "Buyer"},
            "ShippingDetails": {"ShippingType": "Flat", "ShippingServiceOptions": {"ShippingServicePriority": "1", "ShippingService": "USPSMedia", "ShippingServiceCost": "%.2f" % uniform(1, 4)}},
            "Site": "US"}}
        self.api.execute("AddItem", item)

    def randomStr(self,length=10):
        str = ""
        chars = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789"
        romlen = len(chars) - 1
        random = Random()
        for i in range(length):
            str += chars[randint(0, romlen)]
        return str

    def createList(self):
        itemData = self.api.response_dict()
        return {"itemid": itemData["ItemID"]["value"], "link": "http://cgi.sandbox.ebay.com/%s-/%s" % (self.name, itemData["ItemID"]["value"])}

