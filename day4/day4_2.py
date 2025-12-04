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
rolls = {}
for i in range(h):
    for j in range(w):
        if rows[i][j] == '@':
            rolls[i, j] = 0


for i in range(h):
    for j in range(w):
        if rows[i][j] == '.':
            continue
        
        for ii, jj in neighs:
            if (i == 0 and ii == -1) or (i == h-1 and ii == 1):
                continue
            if (j == 0 and jj == -1) or (j == w-1 and jj == 1):
                continue
            rolls[(i,j)] += rows[i+ii][j+jj] != '.'

accessible = {ij: rolls[ij] for ij in rolls if rolls[ij] < 4}
k=len(accessible)
result = 0
while k != 0:
    print(k)
    result += k
    for ij in accessible:
        i = ij[0]
        j = ij[1]
        rolls.pop(ij)
        rows[i][j] = '.'
        # Update neighbors
        for ii, jj in neighs:
            if (i+ii, j+jj) in rolls:
                rolls[(i+ii, j+jj)] -= 1


    accessible = {ij: rolls[ij] for ij in rolls if rolls[ij] < 4}
    k = len(accessible)

print(result)