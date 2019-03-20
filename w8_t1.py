def count(str1):
    a = {}
    for i in str1:
        a[i] = a.get(i,0)+1
           
    for key, value in a.items():
         print("The char ", key, "appears ", value, "times")

def main():
    str1 = str(input("Enter string: "))
    count(str1)

main()

