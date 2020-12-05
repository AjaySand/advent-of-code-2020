from aoc_data import data

for num in data:
    for num_num in data:
        for num_num_num in data:
            if (num_num + num + num_num_num) == 2020:
                print(num * num_num * num_num_num)
                exit()

