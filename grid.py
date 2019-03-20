row = int(input("Number of rows: "))
col = int(input("Number of columns: "))
size = int(input("Grid size: "))
def print_middle():
    for a in range(col):
        print("|" + " "*size,end="")
    print("|")
def print_boundary():
    for b in range(col):
        print("+" + "-"*size,end="")
    print("+")
def main():
    for x in range(row):
        print_boundary()
        for y in range(size):
            print_middle()
    print_boundary()
main()
