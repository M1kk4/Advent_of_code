#Part 1
count_true = 0
count_false = 0
for line in open("2dayinputpasswd.txt"):
    line.split(" ")
    data = line.split(" ")
    KOBE = data[0].split("-")
    min = int(KOBE[0])
    max = int(KOBE[1])
    #print(min,max)
    a = data[1].split(":")
    iskanje = a[0]
    #print(iskanje[0])
    value = data[2]
    #print(value)
    BOB = value.count(iskanje)
    if BOB <= max and BOB >= min:
        count_true += 1
    else:
        count_false += 1
print(count_true)

#Part 2

count_true = 0
count_false = 0
for line in open("2dayinputpasswd.txt"):
    data = line.split(" ")
    KOBE = data[0].split("-")
    min = int(KOBE[0])
    max = int(KOBE[1])
    #print(min,max)
    a = data[1].split(":")
    iskanje = a[0]
    #print(iskanje[0])
    value = data[2]
    if (iskanje == value[min - 1] and iskanje != value[max - 1]) or (iskanje != value[min - 1] and iskanje == value[max - 1]):
        count_true +=1
        #print("isce: " +iskanje+" Enako: " + value[min - 1] + " neenako: " + value[max - 1])
        print(iskanje, value[min - 1], value[max - 1])
    else:
        count_false += 1
print(count_true)
print(count_false)
