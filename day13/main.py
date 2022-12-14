import json
import enum

class Result(enum.Enum):
    FALSE = 0
    TRUE = 1
    CONTINUE = 2

def part1():
    a, b = [], []
    current, prev = a, 'a'
    with open('input.txt') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            current.append(json.loads(line))
            current = b if prev == 'a' else a
            prev = 'b' if prev == 'a' else 'a'

    def compare(x, y):
        i = 0
        while i < len(x) and i < len(y):
            if isinstance(x[i], int) and isinstance(y[i], int):
                if x[i] > y[i]:
                    return Result.FALSE
                if x[i] < y[i]:
                    return Result.TRUE
            elif isinstance(x[i], list) and isinstance(y[i], list):
                res = compare(x[i], y[i])
                if res != Result.CONTINUE:
                    return res
            elif isinstance(x[i], int) and isinstance(y[i], list):
                res = compare([x[i]], y[i])
                if res != Result.CONTINUE:
                    return res
            else:
                res = compare(x[i], [y[i]])
                if res != Result.CONTINUE:
                    return res
        
            i += 1
        
        if len(x) < len(y):
            return Result.TRUE
        if len(x) == len(y):
            return Result.CONTINUE
        return Result.FALSE
        

    matches = []
    i = 0
    while i < len(a):
        if compare(a[i], b[i]) == Result.TRUE:
            matches.append(i + 1)
        i += 1

    print("Match Pairs:", matches)
    print("Sum of pair indicies:", sum(matches))

def part2():
    packets = []
    with open('input.txt') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            packets.append(json.loads(line))
    
    a_divider_idx, b_divider_idx = 1, 2

    def compare(a, num):
        if isinstance(a, list) and a:
            return compare(a[0], num)
        elif isinstance(a, list) and not a:
            return True
        return True if a < num else False

    for i in range(len(packets)):
        if compare(packets[i], 2):
            a_divider_idx += 1
            b_divider_idx += 1
        elif compare(packets[i], 6):
            b_divider_idx += 1
    
    print("[[2]] index:", a_divider_idx)
    print("[[6]] index:", b_divider_idx)
    print("Decoder key:", a_divider_idx * b_divider_idx)


part1()
part2()