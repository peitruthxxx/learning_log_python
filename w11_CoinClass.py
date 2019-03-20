import random
class Coin: #大寫開頭
    def __init__(self): #對物件作初始化，self像是C++裡的this
        self.side_up = "Head"
    def toss_coin(self):
        if self.side_up == "Head":
            self.side_up = "Tail"
        else:
            self.side_up = "Head"
    def random_toss(self):
        rand = random.randint(0,1)
        if rand == 1:
            self.side_up = "Tail"
        elif rand == 0:
            self.side_up = "Head"

class CoinType(Coin): #繼承
    def __init__(self,price):
        super().__init__() #初始化父類別
        self.price = price
    def __str__(self): #可直接查詢物件內容
        return self.price