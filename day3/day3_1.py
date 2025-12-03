def parse_input(fname):
    with open(fname) as f:
        lines = f.readlines()

    banks = []
    for l in lines:
        bank = l.strip('\n')
        bank = [int(b) for b in bank]
        banks.append(bank)
    return banks


banks = parse_input('day3/input.txt')

result = 0
for b in banks:
    nl = max(b[:-1])
    il = b.index(nl)
    nr = max(b[il+1:])
    result += int(f"{nl}{nr}")


print(result)