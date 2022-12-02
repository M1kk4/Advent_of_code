def part1(lines, scores):
    score = 0
    for line in lines:
        score += int(scores[line.strip()])
    return score   

def part2(lines, scores1):
    score = 0
    for line in lines:
        score += int(scores1[line.strip()])
    return score

f = open("2input.txt", "r")
lines = f.readlines()
scores = {"A X" : 4, "A Y" : 8, "A Z" : 3, "B X" : 1, "B Y" : 5, "B Z" : 9, "C X" : 7, "C Y" : 2, "C Z" : 6}
scores1 = {"A X" : 3, "A Y" : 4, "A Z" : 8, "B X" : 1, "B Y" : 5, "B Z" : 9, "C X" : 2, "C Y" : 6, "C Z" : 7}

print(f'Part 1: {part1(lines, scores)}')
print(f'Part 2: {part1(lines, scores1)}')
