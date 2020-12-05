from aoc_data import data

trees = 0
lines = data.splitlines()
#  print(*lines, sep='\n')

x, y = 0, 0
step = {
    'x': 3,
    'y': 1
}

while(True):
    x += step.get('x')
    y += step.get('y')

    if len(lines) <= y:
        print("End of lines")
        break

    if (len(lines[y]) - x) <= 0:
        print("-" * 78)
        x = (len(lines[y]) - x) * -1

    print("len - x: {}, y: {}, x: {} \t char:{} \t line: {}".format(len(lines[y]) - x, y, x, lines[y][x], lines[y]))

    if lines[y][x] == '#':
        trees += 1


print(trees)
