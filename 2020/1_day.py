# Part 1

f = open("code.txt", "r")
numbers = []
for x in f:
    numbers.append(int(x))

data = f.readline()
for line in numbers:
    for bob in numbers:
        if line + bob == 2020:
            answer = line * bob
            print(str(answer))

# Part 2


f = open("code.txt", "r")
numbers = []
for x in f:
    numbers.append(int(x))

data = f.readline()
for line in numbers:
    for bob in numbers:
        for KOBE in numbers:
            if line + bob + KOBE == 2020:
                answer = line * bob * KOBE
                print(str(answer))            

