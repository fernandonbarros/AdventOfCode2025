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

beams = {start: 1}

i = 0
while i < height:
    new_beams = {}
    for b in beams:
        if b in splitters[i]:
            if b-1 in new_beams:
                new_beams[b-1] += beams[b]
            else:
                new_beams[b-1] = beams[b]
            if b+1 in new_beams:
                new_beams[b+1] += beams[b]
            else:
                new_beams[b+1] = beams[b]
        else:
            if b in new_beams:
                new_beams[b] += beams[b]
            else:
                new_beams[b] = beams[b]
    beams = new_beams
    print(f"{i} - {beams}")
    i += 1

print(sum([beams[b] for b in beams]))