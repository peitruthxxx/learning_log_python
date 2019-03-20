import random

limit = 6

def guessing(rand_num, init):
    
    min = 1
    max = 100
    guess_value = init

    if (rand_num > guess_value):
        print("Too low!")
        min = guess_value
        guess_value = int(input("Guess a number from {} to {}: ".format(min, max)))

    elif (rand_num < guess_value):
        print("Too high!")
        max = guess_value
        guess_value = int(input("Guess a number from {} to {}: ".format(min, max)))

    return guess_value

def yon():
    yes_no = str(input(":"))
    while True:
        if yes_no == "y":
            return main()
        else:
            break
    
def main():
    rand_num = random.randint(1,100)
    
    print(rand_num)
    init = int(input("Guess a number from 1 to 100: "))
    for x in range(limit-1):
        init = guessing(rand_num, init)
        
        if init == rand_num:
            print("You passed, next game?")
            yon()
        elif x == limit-2:
            print("Achieve limit, try again?")
            yon()

main()
