import math

def cal(x ,a):
    y = (x + a/x) / 2
    return y
    
def main():
    a = float(input("Enter a value to find square root: "))
    x = 3.0
    
    prev = 0
    curr = cal(x, a)
    while abs(prev - curr) > 0.0000001:
        print(curr)
        prev = curr
        curr = cal(prev, a)

    print(curr)
    print(math.sqrt(a))

main()

#目的：利用牛頓法求平方根近似值
#利用迴圈無限逼近root值 前後值相差<0.0000001時跳出迴圈
#再印出sqrt函數值

"""
#YC另一個寫法 
import math
PRECISION = 10 ** -8
def estimate(target, x = 1):
  while True:
    x = (x + target / x) / 2
    yield x

def main():
  sqrtOfFive = estimate(5) #input
  prev, now = 0, next(sqrtOfFive)
  while abs(now - prev) > PRECISION:
    prev, now = now, next(sqrtOfFive)
  print(now)
  print(math.sqrt(5))

if __name__ == '__main__':
  main()
"""