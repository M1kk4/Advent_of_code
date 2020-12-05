def id_seat(lines):
    list = []
    for line in lines:
        row = int(line[:-3].replace("F", "0").replace("B", "1"),2)
        column = int(line[-3:].replace("L", "0").replace("R", "1"),2)
        sid = row * 8 + column
        list.append(sid)
    return list
def my_seat(lines):
    for i in range(len(lines) -1):
        if abs(lines[i] - lines[i + 1]) == 2:
            return (lines[i] + lines[i + 1])/2

lines = open("plane.txt", "r").read().rsplit()

print(max(id_seat(lines)))
print(int(my_seat(sorted(id_seat(lines)))))
