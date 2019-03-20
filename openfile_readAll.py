open_file = open('test.txt','r')

for line in open_file:
    line = line.rstrip('\n')
    print(line)