import math

#  testData = open("day-05/testData.txt", "r")
data = open("day-05/data.txt", "r")
#  data = testData

# example: bfffbbf
# start = 0, end = 127
# walk steps
# b -> 64 - 127
# f -> 64 - 95
# f -> 64 - 79
# f -> 64 -  71 (79 - ((79 - 64) // 2))
# b -> 68 (64 + ((71 - 64) // 2)) - 71
# b -> 69 (68 + ((71 - 68) // 2)) - 71
# f -> 70 (69 + ((71 - 69) // 2)) - 70

def walk(path: str, minim:int, maxmum:int, top_str:str) -> int:
    start = minim
    end = maxmum

    for char in path:
        if(char == top_str):
            start = math.ceil(start + ((end - start) / 2))
        else:
            end = math.ceil(end - ((end - start) / 2))

        #  print("{} ---  start: {}, end: {}".format(char, start, end))

    #  print("\n\n")
    return start

lines = data.readlines()
highest = 0

for line in lines:
    line = line.strip()

    row = walk(line[:7], 0, 127, 'B')
    #  print('row: ', row)

    col = walk(line[7:len(line)], 0, 7, 'R')

    #  print('col: ', col)
    seat_id = row * 8 + col
    if(seat_id > highest):
        highest = seat_id

    print("seat: {}, row: {}, col: {}".format(seat_id, row, col))
    pass

print("highest: {}".format(highest))
