class computer:
    def __init__(self):
        self.__maxprice = 900
    def sell(self):
        print("The selling Price is:",self.__maxprice)
    def setmaxprice(self,price):
        self.__maxprice = price

c = computer()
c.sell()
c.__maxprice = 1000
c.sell()
c.setmaxprice(2000)
c.sell()