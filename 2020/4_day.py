def return_documents():
    f = open("pasport.txt", "r")
    documents = [{}]
    index = 0
    for line in f:
        line = line.rstrip()
        if line == "":
            index = index + 1
            documents.append({})
        else:
            line = line.split()
            for element in line:
                element = element.split(":")
                documents[index][element[0]] = element[1]
    return documents

def count_valid_passports(fields, count = 0):
    for document in return_documents():
        count += all(f in document for f in fields)
    return count

def data_velidation(eye_color, fields, hair_color):
    count = 0
    for document in return_documents():
        if all(f in document for f in fields):
            hgt = document["hgt"]
            value, unit = hgt[:-2], hgt[-2:]
            hcl = document["hcl"]
            if int(document["byr"]) <= 2002 and int(document["byr"]) >= 1920:
                if int(document["iyr"]) <= 2020 and int(document["iyr"]) >= 2010:
                    if int(document["eyr"]) <= 2030 and int(document["eyr"]) >= 2020:
                        if any(f in document["ecl"] for f in eye_color):
                            if len(document["pid"]) == 9:
                                if (unit == "cm" and int(value) <=193 and int(value)>= 150) or (unit == "in"and int(value) <=76 and int(value)>= 59):
                                    if hcl[0] == "#" and all(c in '0123456789abcdef' for c in hcl[1:]):
                                        count += 1
    return count
fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
eye_color = ['amb', 'blu', 'brn','gry','grn','hzl','oth']
hair_color = ["#",0,1,2,3,4,5,6,7,8,9,"a","b","c","d","e","f",]
print(count_valid_passports(fields)) #part 1
print(data_velidation(eye_color,fields,hair_color)) #part 2
