def parse_input(fname):
    with open(fname) as f:
        lines = f.readlines()

    splitters = []
    for l in lines:
        l = l.strip('\n')
        sps = [i for i in range(len(l)) if l[i] == '^']
        splitters.append(sps)

    start = lines[0].find('S')
    return splitters, start

def step(pos, splitters, row=0):
    total = 0
    if row == len(splitters):
        return 1
    if pos in splitters[row]:
        total += step(pos-1, splitters, row+1)
        total += step(pos+1, splitters, row+1)
    else:
        total += step(pos, splitters, row+1)
    return total


splitters, start = parse_input('day7/input.txt')

print(step(start, splitters, row=0))