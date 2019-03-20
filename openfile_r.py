def main():
    infile = open('test.txt','r')

    line1 = infile.readline() 
    line2 = infile.readline()
    line3 = infile.readline()

    line1 = line1.rstrip('\n') #刪除換行
    line3 = line3.rstrip('\n')

    print(line1)
    print(line2)
    print(line3)

main()