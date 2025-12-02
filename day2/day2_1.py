def parse_input(fname):
    with open(fname) as f:
        line = f.readline()

    line.strip("\n")
    ranges = line.split(',')
    result = []
    for r in ranges:
        rs, re = r.split('-')
        result.append((rs, re))
    
    return result

def simplify_ranges(ranges):
    simple_ranges = []

    for r in ranges:
        rs = r[0]
        re = r[1]
        dl = len(re) - len(rs)
        for i in range(dl+1):
            ree = min(int(re), 10**(len(rs))-1)
            if (len(rs) % 2) == 0:
                simple_ranges.append((rs, str(ree)))
            rs = str(ree+1)
    return simple_ranges

def find_invalid(ranges):
    invalid = []
    for r in ranges:
        rs = r[0]
        re = int(r[1])

        rs_half = rs[:len(rs)//2]
        invalid += next_digit('', int(rs), re, first_digit=int(rs_half[0]))
    return invalid
        
def next_digit(digits, rs, re, first_digit=0):
    result = []

    for k in range(first_digit, 10):
        n = digits + str(k)

        if len(str(re)) < 2*len(n):
            return result

        if len(str(re)) == 2*len(n):
            if (int(2*n) >= int(rs)) & (int(2*n) <= re):
                result.append(2*n)

        res = next_digit(n, rs, re)
        # if res == []:
        #     break
        result += res

    return result


ranges = parse_input('day2/input.txt')
print(ranges)
print('------')

simple_ranges = simplify_ranges(ranges)
print(simple_ranges)
print('------')

invalid = find_invalid(simple_ranges)
print(invalid)

invalid = [int(n) for n in invalid]
invalid.sort()
print(sum(invalid))