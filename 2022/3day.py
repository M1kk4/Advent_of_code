def part1(lines):
    value = 0
    for line in lines:
        firsthalf = line[:int(len(line)/2)]
        secondthalf = line[int(len(line)/2):]
        for x in range(len(firsthalf)):
            if firsthalf[x] in secondthalf:
                if firsthalf[x].islower():
                    value += ord(firsthalf[x]) - 96
                else:
                    value += ord(firsthalf[x]) - 38
                break
    return value

def part2(lines):
    value = 0
    for line in range(0, len(lines), 3):
        for character in lines[line]:
            if character in lines[line + 1] and character in lines[line + 2]:
                if character.islower():
                    value += ord(character) - 96
                else:
                    value += ord(character) - 38
                break
    return value


f = open("3input.txt", "r")
lines = f.readlines()

print(f"Answer to part1 is: {part1(lines)}")
print(f"Answer to part2 is: {part2(lines)}")
