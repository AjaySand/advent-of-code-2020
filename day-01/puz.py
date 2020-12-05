from aoc_data import data

for num in data:
    for num_num in data:
        if num_num + num == 2020:
            print(num * num_num)
            exit()

