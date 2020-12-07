import re

testData = open("testData.txt", "r")
data = open("data.txt", "r")
#  data = testData

# Validation functions
def validate_byr(val: str) -> bool:
    return (len(val) == 4 and int(val) >= 1920 and int(val) <= 2002)


def validate_iyr(val: str) -> bool:
    return (len(val) == 4 and int(val) >= 2010 and int(val) <= 2020)


def validate_eyr(val: str) -> bool:
    return (len(val) == 4 and int(val) >= 2020 and int(val) <= 2030)


def validate_hgt(val: str) -> bool:
    if "cm" in val:
        i_val = int(val[:len(val)-2])
        return (i_val >= 150 and  i_val <= 193)
    elif "in" in val:
        i_val = int(val[:len(val)-2])
        return (i_val >= 59 and  i_val <= 76)
    else:
        return False


def validate_hcl(val: str) -> bool:
    regex = re.compile('^#[0-9a-fA_F]{6}')
    return bool(regex.match(val))

def validate_ecl(val: str) -> bool:
    valid_eye_colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    return val in valid_eye_colors


def validate_pid(val: str) -> bool:
    return len(val) == 9

conditions = {
    "byr": {"validator": validate_byr, "valid": False},
    "iyr": {"validator": validate_iyr, "valid": False},
    "eyr": {"validator": validate_eyr, "valid": False},
    "hgt": {"validator": validate_hgt, "valid": False},
    "hcl": {"validator": validate_hcl, "valid": False},
    "ecl": {"validator": validate_ecl, "valid": False},
    "pid": {"validator": validate_pid, "valid": False},
}

dataLines = 0
emptlyLines = 0
valid = 0

lines = data.readlines()
lines.append("\n")
for i, line in enumerate(lines):
    l = line.strip()

    if len(l) == 0 or i >= len(lines):
        emptlyLines += 1
        # check conditions and increment valid
        if all(v['valid'] for v in conditions.values()):
            valid += 1

        # reset conditions
        for key in conditions:
            conditions[key]["valid"] = False

    else:
        dataLines +=1
        lineData = l.split(' ')
        for val in lineData:
            if conditions.get(val[:3]) != None:
                conditions[val[:3]]["valid"] = conditions[val[:3]]["validator"](val[4:len(val)])


data.close()
print("Number of valid 'passports': {}".format(valid))
print("Number of parsed lines: {}".format(dataLines))
print("Number of empty lines: {}".format(emptlyLines -1))
print("Number of total lines: {}".format(len(lines) -1))
