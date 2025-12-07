import numpy as np

def parse_input(fname):
    with open(fname) as f:
        lines = f.readlines()

    lines = [list(l.strip('\n')) for l in lines]
    
    return np.array(lines)


m = parse_input('day6/input.txt')
m = m.T


op = None
ns = []
total = 0
print(m)
for i in range(len(m)):
    if (m[i] == ' ').all():
        expr = str(op).join(ns)
        total += eval(expr)
        print(expr)
        continue

    if m[i][-1] in '+*':
        op = m[i][-1]
        ns = [''.join(m[i][:-1].tolist())]
    else:
        ns.append(''.join(m[i][:-1].tolist()))
      
expr = str(op).join(ns)
total += eval(expr)
print(total)