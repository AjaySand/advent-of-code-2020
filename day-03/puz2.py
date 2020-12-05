from aoc_data import data

lines = data.splitlines()
#  print(*lines, sep='\n')

steps = [
    {'x': 1, 'y': 1},
    {'x': 3, 'y': 1},
    {'x': 5, 'y': 1},
    {'x': 7, 'y': 1},
    {'x': 1, 'y': 2}
]

mult = 1

for step in steps:
    trees = 0
    x, y = 0, 0

    while(True):
        x += step.get('x')
        y += step.get('y')

        if len(lines) <= y:
            #  print("End of lines")
            break

        if (len(lines[y]) - x) <= 0:
            #  print("-" * 78)
            x = (len(lines[y]) - x) * -1

        #  print("len - x: {}, y: {}, x: {} \t char:{} \t line: {}".format(len(lines[y]) - x, y, x, lines[y][x], lines[y]))

        if lines[y][x] == '#':
            trees += 1


    mult *= trees
    print(trees)
print("mult: {}".format(mult))
