import re

def parse_input(fname):
    with open(fname) as f:
        lines = f.readlines()

    numbers = []
    for l in lines:
        if '*' in l:
            ops = [o for o in re.split(r" +", l.strip(' \n'))]
        else:
            for i, n in enumerate(re.split(r" +", l.strip(' \n'))):

                if len(numbers) == i:
                    numbers.append([n])
                else:
                    numbers[i].append(n)

    return numbers, ops

numbers, ops = parse_input('day6/input.txt')

total = 0
for i, o in enumerate(ops):
    result = eval(o.join(numbers[i]))
    total += result
    # print(result)

print(total)