level = int(input("Please enter a value: "))

for x in range(level):
    print("#",end="")
    for y in range(0,x):
        print(" ",end="")
    print("#")
"""
user_input = int(input("Please enter a value:"))
for i in range(user_input):
    print("#"+" "*i + "#)
"""