def id_seat(lines):
    list = []
    for line in lines:
        row = int(line[:-3].replace("F", "0").replace("B", "1"),2)
        column = int(line[-3:].replace("L", "0").replace("R", "1"),2)
        sid = row * 8 + column
        list.append(sid)
    return list
def my_seat(lines):
    for line in sorted(id_seat(lines)):
        for line_2 in sorted(id_seat(lines)):
            if line - line_2 == 2:
                return (line + line_2)/2

lines = open("plane.txt", "r").read().rsplit()

print(max(id_seat(lines)))
print(my_seat(lines))
