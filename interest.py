interest = int(input("利潤："))
money = 0
arr_i = [1000000,600000,400000,200000,100000,0]
arr_r = [0.01,0.015,0.03,0.05,0.075,0.1]

for x in range(0,6):
    if interest > arr_i[x]:
        money += (interest-arr_i[x])*arr_r[x] #interest>100萬的時候，扣掉100萬再乘以％數
        print(money)
        interest =  arr_i[x] #高出10w/20w/40w/60w的部分
print ("獎金：",money)