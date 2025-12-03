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
n_bats = 12

for b in banks:
    last_n = None
    bats = ''
    count = 0
    i = -1
    while count < n_bats:
        i0 = i+1
        ie = len(b) - n_bats + count + 1
        n = max(b[i0:ie])
        i = i0 + b[i0:ie].index(n)
        bats = f"{bats}{n}"
        count += 1
    print(bats)
    result += int(bats)


print(result)