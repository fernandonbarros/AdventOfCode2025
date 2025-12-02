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

# def simplify_ranges(ranges):
#     simple_ranges = []

#     for r in ranges:
#         rs = r[0]
#         re = r[1]
#         dl = len(re) - len(rs)
#         for i in range(dl+1):
#             ree = min(int(re), 10**(len(rs))-1)
#             if (len(rs) % 2) == 0:
#                 simple_ranges.append((rs, str(ree)))
#             rs = str(ree+1)
#     return simple_ranges

def find_invalid(digits, rs, re):
    ls = len(str(rs))
    le = len(str(re))
    result = []
    if len(digits) > le//2:
        return result
    # Iterage 0 to 9
    for i in range(10):
        if digits == '' and i == 0:
            continue
        # Check if repetition of digits is in range
        n = f"{digits}{i}"
        for k in range(2, le//len(n)+1):
            if rs <= int(k*n) <= re:
                result.append(int(k*n))
        
            # Recursion
        result += find_invalid(n, rs, re)

    return result



ranges = parse_input('day2/input.txt')
print(ranges)
print('------')

invalid = []
for r in ranges:
    rs = int(r[0])
    re = int(r[1])

    res = find_invalid('', rs, re)
    invalid += res

print(sum(set(invalid)))
