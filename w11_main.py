from w11_CoinClass import Coin
from w11_CoinClass import CoinType

coin1 = Coin()
coin2 = Coin()
print(coin1.side_up)
coin1.side_up = "Tail"
print(coin1.side_up)
#for i in range(0,9):
 #   coin1 = coin1.random_toss()
  #  print(coin1.side_up)

coin10 = CoinType(10) #初始化為10元硬幣
print(coin10.price,coin10.side_up)
coin10.toss_coin()
print(coin10.price,coin10.side_up)