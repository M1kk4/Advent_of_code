def bob(lines, right, down):
    trees = 0
    x = 0
    for i in range(0, len(lines), down):
        line = lines[i].rstrip()
        x = x % len(line)
        if line[x] == "#":
            trees += 1
        x = x + right
    return trees
f = open("trees.txt", "r")
lines = f.readlines()
print(bob(lines,3,1)) #part 1
print(bob(lines,1, 1)*bob(lines,3, 1)*bob(lines,5, 1)*bob(lines,7, 1)*bob(lines,1, 2)) #part 2
