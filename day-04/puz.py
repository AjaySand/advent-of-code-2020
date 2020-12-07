#  testData = open("testData.txt", "r")
data = open("data.txt", "r")

requiredFilds = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]

conditions = {
    "byr": False,
    "iyr": False,
    "eyr": False,
    "hgt": False,
    "hcl": False,
    "ecl": False,
    "pid": False,
    #  "cid": False
}

valid = 0
dataLines = 0
emptlyLines = 0

lines = data.readlines()
lines.append("\n")
for i, line in enumerate(lines):
    l = line.strip()

    if len(l) == 0 or i >= len(lines):
        emptlyLines += 1
        # check conditions and increment valid
        if all(v == True for v in conditions.values()):
            valid += 1

        # reset conditions
        for key in conditions:
            conditions[key] = False

    else:
        dataLines +=1
        lineData = l.split(' ')
        for val in lineData:
            if conditions.get(val[:3]) != None:
                conditions[val[:3]] = True

data.close()
print("Number of valid 'passports': {}".format(valid))
print("Number of parsed lines: {}".format(dataLines))
print("Number of empty lines: {}".format(emptlyLines -1))
print("Number of total lines: {}".format(len(lines) -1))
