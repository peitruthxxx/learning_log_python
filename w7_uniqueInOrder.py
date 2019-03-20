def unique_in_order(letters):
    alpha = []
    for i in range(-1,len(letters)):
        if (letters[i-1] != letters[i]):
            alpha.append(letters[i])
    print(alpha)


def main():
    letters = 'BBCCCDDAAB'
    unique_in_order(letters)

main()
