def check(pwd):
    rules = [ lambda pwd: any(x.isupper() for x in pwd),
              lambda pwd: any(x.islower() for x in pwd),
              lambda pwd: any(x.isdigit() for x in pwd),
              lambda pwd: len(pwd)>=10
            ]
    if rules[0](pwd) and rules[1](pwd) and rules[2](pwd) and rules[3](pwd):
        print("Valid!")
    for i in range(len(rules)):
        if rules[i](pwd) is False:
            if i == 0:
                print("Must have at least one upperCase!")
            elif i == 1:
                print("Must have at least one lowerCase!")
            elif i == 2:
                print("Must have at least one number!")
            elif i == 3:
                print("Length must longer than 10 character!")

def main():
    pwd = str(input("Enter password: "))
    check(pwd)

main()