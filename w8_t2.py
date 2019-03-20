dict_champ = {}
infile = open('WorldSeriesWinners.txt','r')
i = 1903

while (i < 2017):
    if i == 1904:
        dict_champ[i] = " "
    elif i == 1994:
        dict_champ[i] = " "
    else:
        line = infile.readline().rstrip('\n')
        dict_champ[i] = line
    i += 1

def team_name():
    count = 0
    try:
        team = str(input("Enter Championship team:"))
        for key, value in dict_champ.items():
            if team == value:
                print(key)
                count += 1
        print('The team win ',count,' times.')
    except ValueError:
        if not team:
            raise ValueError('Empty String')
        else:
            raise ValueError('not String')
def team_champ_times():
    print('')
def main():
        choose = int(input("1.隊名\n2.冠軍次數\n"))
        if choose == 1:
            team_name()
        elif choose == 2:
            print(' ')
        else:
            exit()

main()