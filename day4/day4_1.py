def parse_input(fname):
    with open(fname) as f:
        lines = f.readlines()

    rows = [[p for p in l.strip('\n')] for l in lines]

    return rows

rows = parse_input('day4/input.txt')

def add_neighbor(ij, neighbors):

    if ij not in neighbors:
        neighbors[ij] = 1
    else:
        neighbors[(ij)] += 1
    
    return neighbors
h, w = len(rows), len(rows[0])
accessible = []
neighs = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1), (0, 1),
    (1, -1), (1, 0), (1, 1)
]


for i in range(len(rows)):
    row = rows[i]
    for j in range(len(row)):
        count = 0

        if row[j] == '.':
            continue
        for ii, jj in neighs:
            if (i == 0 and ii == -1) or (i == h-1 and ii == 1):
                continue
            if (j == 0 and jj == -1) or (j == w-1 and jj == 1):
                continue
            count += rows[i+ii][j+jj] != '.'
            if count >= 4: break
        if count < 4:
            accessible.append((i, j))
            rows[i][j] = 'x'
    print(''.join(row))
    
print(len(accessible))