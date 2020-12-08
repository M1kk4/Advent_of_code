def accumulator(lines):
    id = 0
    already_been = []
    accumulator = 0

    while id not in already_been:
        line = lines[id].split()
        already_been.append(id)

        if line[0] == "acc":
            accumulator += int(line[1])
            id += 1

        elif line[0] == "jmp":
            id += int(line[1])

        else:
            id += 1

    return accumulator

def fixed_code(lines,id=0,value = 0,previous_command=set(),switch=True):
    if not (-1 < id < len(lines)):
        return value

    if id in previous_command:
        return None

    line = lines[id].split()

    previous_command.add(id)

    if line[0] == "acc":
        return fixed_code(lines,id+1,value + int(line[1]), previous_command, switch)

    elif line[0] == "jmp":
        result = fixed_code(lines,id +int(line[1]),value,previous_command,switch)

        if result == None and switch == True:
            return fixed_code(lines,id + 1,value,previous_command,False)

        return result

    else:
        result = fixed_code(lines, id + 1, value, previous_command, switch)

        if result == None and switch == True:
            return fixed_code(lines, id + int(line[1]), value, previous_command, False)

        return result

f = open("instructions.txt", "r")
lines = f.readlines()

print(accumulator(lines)) #part 1
print(fixed_code(lines)) #part 2
