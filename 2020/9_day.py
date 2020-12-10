def invalid_number(lines): # part 1
    i = 0
    j = 25
    while j < len(lines):

        if not find_right_numbers(lines[i:j], lines[j]):
            return lines[j]
        i += 1
        j += 1

def find_right_numbers(list,next_number):
    for element in list:
        if (next_number - element) in list:
            return True
    return False

input = [int(i.strip()) for i in open("sum_num.txt", "r").readlines()]

print(invalid_number(input))
