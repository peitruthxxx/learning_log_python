import random

def main():
    filename = str(input("Please specify filename: "))
    outfile = open(filename, 'w')

    try:
        amount = int(input("Please enter amount of data: "))
        for i in range(amount):
            number = random.randint(1,500)
            outfile.write(str(number))
            outfile.write('\n')
    except:
        print("Non-integer entered!")
    
    outfile.close()

main()
