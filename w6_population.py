
def main():
    with open('USPopulation.txt','r') as openfile:
        population = [line.strip() for line in openfile]
        population = list(map(int, population))
        print(population)
    print("總人口數：",sum(i for i in population))
    for i in range(1950,1990):
        
main()
