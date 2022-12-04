def part1(lines):
    count = 0
    for line in lines:
        split = line.split(",")
        first = split[0].split("-")
        second = split[1].strip().split("-")
        elf1 = {int(num) for num in range(int(first[0]), int(first[1])+1)}
        elf2 = {int(num) for num in range(int(second[0]), int(second[1]) + 1)}
        count += elf1.issubset(elf2) or elf2.issubset(elf1)
    return count

def part2(lines):
    count = 0
    for line in lines:
        split = line.split(",")
        first, second = split[0].split("-"), split[1].strip().split("-")
        elf1 = {int(num) for num in range(int(first[0]), int(first[1]) + 1)}
        elf2 = {int(num) for num in range(int(second[0]), int(second[1]) + 1)}
        count += len(elf1.intersection(elf2)) > 0
    return count

f = open("4day.txt", "r")
lines = f.readlines()

print(f"Answer to part 1: {part1(lines)}")
print(f"Answer to part 2: {part2(lines)}")
