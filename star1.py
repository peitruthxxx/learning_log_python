level = int(input("Please enter a value: "))

for a in range(level):
    for b in range(level, a, -1):
        print("*",end="")
    print("\n")
for a in range(level-1):
    for c in range(0, a+2):
        print("*",end="")
    print("\n")