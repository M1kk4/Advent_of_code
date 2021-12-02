def part1(numbers):
    count = 0
    for a in range(len(numbers)-1):
        if numbers[a] < numbers[a + 1]:
            count += 1
    print(f"Answer to part 1: {count}")

def part2(numbers):
    count = 0
    for a in range(len(numbers) - 3):
        if numbers[a] < numbers[a+3]:
            count += 1
    print(f"Answer to part 2: {count}")

f = open("1day.txt")
numbers = []
for x in f:
    numbers.append(int(x))
    
part1(numbers)
part2(numbers)
