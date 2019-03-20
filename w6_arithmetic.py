def add(x, y):
    print(x+y)

def sub(x, y):
    print(x-y)

def mul(x, y):
    print(x*y) 

def div(x, y):
    print(x/y)

def main():
    choose = int(input("Enter number 0-3: "))
    x = int(input("x: "))
    y = int(input("y: "))

    func = [add, sub, mul, div]
    
    func[choose]

main()


    