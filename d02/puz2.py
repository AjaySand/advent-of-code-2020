from aoc_data import data

num_valid = 0
for d in data:
    mn, mx = d.get('min') -1, d.get('max') -1

    #  print(mn, mx, len(d['passwd']), mn <= len(d['passwd']), mx <= len(d['passwd']))
    s = d.get('passwd')
    if (s[mn] == d.get('letter') or s[mx] == d.get('letter')) and not (s[mn] == s[mx]):
        num_valid += 1

print(num_valid)

