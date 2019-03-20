while True:
    num = int(input("Please enter an odd number: "))
    level = int(num/2+0.5)
    
    if num % 2 == 0:
        continue
    
    for x in range(level):
        for y in range(level-1, x, -1):
            print(" ",end="")
        for z in range(0, 2*x+1, 1):
            print("*",end="")
        print("\n")
    for x in range(level-1):
        for y in range(0, x+1):
            print(" ",end="")
        for z in range(num-2, x*2, -1):
            print("*",end="")
        print("\n")

    break