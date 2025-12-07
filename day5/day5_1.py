def parse_input(fname):
    with open(fname) as f:
        lines = f.readlines()

    ranges = []
    ingredients = []

    for l in lines:
        if '-' in l:
            start, end = l.strip('\n').split('-')
            ranges.append((int(start), int(end)))
        elif l=='\n':
            continue
        else:
            ingredients.append(int(l.strip('\n')))

    return ranges, ingredients

ranges, ingredients = parse_input('day5/input.txt')

print(ranges)
print(ingredients)

# Sort ranges
ranges = sorted(ranges, key=lambda x: x[0])

# Sort ingredients
ingredients = sorted(ingredients)

n_ingredients = len(ingredients)
fresh = []
# Iterate through ranges
i = 0
for r in ranges:
    while i < n_ingredients:
        if ingredients[i] > r[1]:
            break
        if r[0] <= ingredients[i] <= r[1]:
            fresh.append(ingredients[i])
        i += 1
print(fresh)
print(len(fresh))
