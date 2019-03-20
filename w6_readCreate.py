# 3個exception No choice!(except) Non-integer entered!(value except) Error when opening file!(IOError)
#read file
#Calculate total/average/standard deviation ＝ 總和、平均、標準差
#Find a specific number
import math
def calc(numbers):
    sum_num = sum(numbers)
	amount = len(numbers)
    
def find():

def main():
    filename = input("Please enter filename: ")
    try:
        file1 = open(filename,'r')
        numbers = list(map(lambda x: int(x), file1.readlines()))
    except:
        print("Failed to open file")
    


main()
