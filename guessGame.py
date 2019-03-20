import random
limit = 6

def guess(min, max):
    rand_num = random.randint(1,100)
    print(rand_num)
        
    for x in range(limit):
        guess_value = int(input("guess a number from {} to {}: ".format(min, max)))
        if rand_num > guess_value:
            print("Too low!")
            min = guess_value
        elif rand_num < guess_value:
            print("Too high!")
            max = guess_value
        elif(rand_num == guess_value):
            print("You passed, next game? ")
            break
        max = max
        min = min

    yon = str(input("Try again?"))
    if yon == "y":
        return True
    elif yon == "n":
        return False
    
def main():
    min = 1
    max = 100
    
    again_flag = guess(min, max)
    if again_flag ==  True:
        guess(min, max)
        again_flag = guess(min, max)
    elif again_flag == False:
        print("End")

main()