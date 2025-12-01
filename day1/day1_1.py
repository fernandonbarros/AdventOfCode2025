def parse_input(fname):
    with open(fname) as f:
        lines = f.readlines()

    steps = []
    for l in lines:
        l = l.strip("\n")
        d, n = l[0], int(l[1:])
        steps.append({'dir': d, 'n': n})
    return steps

steps = parse_input('day1/input.txt')

pos = 50
count = 0

for s in steps:
    d_s = s['dir']
    d = 1 if d_s == 'R' else -1 
    n = s['n']
    pos = pos + d*n
    count += (pos % 100) == 0
    print(pos)

print(f"Count = {count}")