def parse_input(fname):
    with open(fname) as f:
        lines = f.readlines()

    splitters = []
    for l in lines:
        l = l.strip('\n')
        sps = [i for i in range(len(l)) if l[i] == '^']
        splitters.append(sps)

    start = lines[0].find('S')
    return splitters, start, len(l)

splitters, start, height = parse_input('day7/input.txt')
print(splitters)

beams = {start}

i = 0
count = 0
while i < height:
    new_beams = set()
    for b in beams:
        print(f"({i}, {b})")
        if b in splitters[i]:
            new_beams.update([b-1, b+1])
            count += 1
        else:
            new_beams.add(b)
    beams = new_beams
    i += 1

print(count)