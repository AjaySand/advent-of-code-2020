import math

data = open("day-05/data.txt", "r")
#  testData = open("day-05/testData.txt", "r")
#  data = testData

def bi_search(ticket: str, minim:int, maxmum:int, top_str:str) -> int:
    start = minim
    end = maxmum

    for char in ticket:
        if(char == top_str):
            start = math.ceil(start + ((end - start) / 2))
        else:
            end = math.ceil(end - ((end - start) / 2))

    return start

lines = data.readlines()
seats = []

for line in lines:
    line = line.strip()
    seats.append(bi_search(line[:7], 0, 127, 'B') * 8 + bi_search(line[7:len(line)], 0, 7, 'R'))

seats = sorted(seats)
empty = None
for i in range(len(seats) - 2):
    #  print("current: {}, +1: {}, i+1: {}".format(seats[i], seats[i] +1, seats[i+1]))
    if (seats[i] + 1) != seats[i+1]:
        empty = seats[i] + 1
        break

print("Empty seat: ", seats[i] + 1)
