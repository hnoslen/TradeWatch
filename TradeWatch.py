# TradeWatch
class TradeWatch:
    def __init__(self):
        self.assets = []
    def addAsset(self,toadd):
        self.assets.append(toadd)
    def rmAsset(self,roremove):
        self.assets.remove(toremove)

class Asset:
    def __init__(self,Name,BoughtPrice,Shares,tradecost):
        self.name = Name
        self.boughtPrice = boughtPrice
        self.shares = shares
        self.currentPrice = None
        self.sellPrice = None
        self.percentChangeToSell = None
        self.buysellcost = tradecost
    def setCurrentPrice(self,CurrentPrice):
        self.currentPrice = CurrentPrice
    def calcSellMinimum(self):
        self.sellPrice = self.boughtPrice+(self.buysellcost/self.shares)
        return self.sellPrice
    def calcPercentChangeToSell(self):
        assert self.currentPrice != None
        assert self.sellPrice != None
        self.percentChangeToSell = (self.sellPrice-self.currentPrice)/self.currentPrice
        return self.percentChangeToSell
    
