from aoc_data import data

#  print('Formated data from Advent of code:', *data, sep='\n- ')

#  {'min': 2, 'max': 9, 'letter': 't', 'pass': 'cntttttcgtttt'},
def get_reps_prase(phrase):
    reps = {}
    for char in phrase:
        #  print("Looking for {char}", reps)
        if reps.get(char) == None:
            reps.update({char: 0})

        reps[char] += 1
    return reps


num_valid = 0
for d in data:
    reps = get_reps_prase(d['passwd'])
    if (reps.get(d['letter']) != None and d['min'] <= reps[d['letter']] <= d['max']):
        num_valid += 1

print(num_valid)

