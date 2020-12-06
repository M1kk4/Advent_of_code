def unique_answers(): #part 1
    answer = 0
    f = open("answers.txt").read()
    groups = f.split("\n\n")
    for group in groups:
        group = group.replace("\n","")
        answer += len(set(group))
    return answer

def same_answers(): #part 2
    result = 0
    f = open("answers.txt").read()
    groups = f.split("\n\n")
    for group in groups:
        group = group.splitlines()
        common_answers = set(group[0])
        for answers in group:
            common_answers = common_answers & set(answers)
        result += len(common_answers)
    return result

print(unique_answers())
print(same_answers())
