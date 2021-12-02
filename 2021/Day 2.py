def part1(lines):
    depth = 0
    horizontal = 0
    for line in lines:
        i = line.rstrip("\n").split(" ")
        axis = i[0]
        value = int(i[1])
        if axis == "down":
            depth += value
        elif axis == "up":
            depth -= value
        else:
            horizontal += value
    return depth * horizontal

def part2(lines):
    aim = 0
    depth = 0
    horizontal = 0
    for line in lines:
        i = line.rstrip("\n").split(" ")
        axis = i[0]
        value = int(i[1])
        if axis == "down":
            aim += value
        elif axis == "up":
            aim -= value
        else:
            horizontal += value
            depth += aim * value
    return depth * horizontal

f = open("2day.txt", "r")
lines = f.readlines()

print(f"Answer to part 1 is: {part1(lines)}")
print(f"Answer to part 2 is: {part2(lines)}")
