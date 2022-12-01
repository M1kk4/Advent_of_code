def part1(data, totalcalories = [], currentcalories = 0):
    for i in data:
        try:
            currentcalories += int(i)            
        except:
            totalcalories.append(currentcalories)
            currentcalories = 0
    print(max(totalcalories))

def part2(data, totalcalories = [], currentcalories = 0):
    for i in data:
        try:
            currentcalories += int(i)            
        except:
            totalcalories.append(currentcalories)
            currentcalories = 0
    totalcalories.sort()
    print(sum(totalcalories[-3:]))

f = open("1input.txt", "r")
data = [line.strip() for line in f]

part1(data, totalcalories = [], currentcalories = 0)
part2(data, totalcalories = [], currentcalories = 0)
