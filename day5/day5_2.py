def parse_input(fname):
    with open(fname) as f:
        lines = f.readlines()

    ranges = []
    ingredients = []

    for l in lines:
        if '-' in l:
            start, end = l.strip('\n').split('-')
            ranges.append([int(start), int(end)])
        elif l=='\n':
            continue
        else:
            ingredients.append(int(l.strip('\n')))

    return ranges, ingredients

ranges, ingredients = parse_input('day5/input.txt')

print(ranges)
# print(ingredients)

# Sort ranges
ranges = sorted(ranges, key=lambda x: x[0])


n_ingredients = len(ingredients)
simplified_ranges = []
# Iterate through ranges
i=0
previous_range=(0,0)
for i, r in enumerate(ranges):
    # Outside - new
    if r[0] > previous_range[1]:
        simplified_ranges.append(r)
    # Contained - continue
    elif r[1] <= previous_range[1]:
        continue
    # Overlap - merge
    else:
        simplified_ranges[-1][1] = r[1]
    previous_range = r

n = 0
for r in simplified_ranges:
    n += r[1]-r[0]+1
print(n)