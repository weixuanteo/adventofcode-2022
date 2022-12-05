def part1():
    stacks = [
        ["N", "R", "G", "P"],
        ["J", "T", "B", "L", "F", "G", "D", "C"],
        ["M", "S", "V"],
        ["L", "S", "R", "C", "Z", "P"],
        ["P", "S", "L", "V", "C", "W", "D", "Q"],
        ["C", "T", "N", "W", "D", "M", "S"],
        ["H", "D", "G", "W", "P"],
        ["Z", "L", "P", "H", "S", "C", "M", "V"],
        ["R", "P", "F", "L", "W", "G", "Z"]
    ]

    # Read actions from input.txt
    with open("input.txt") as f:
        # read from line 11 onwards
        for line in f.readlines()[10:]:
            line = line.strip()
            # Split line (move X from X to X) into count, from, to
            line = line.split(" ")
            count, frm, to = int(line[1]), int(line[3]), int(line[5])
            for i in range(count):
                stacks[to - 1].append(stacks[frm - 1].pop())
    
    res = ""
    for stack in stacks:
        res += stack[-1]
    
    print(res)

def part2():
    stacks = [
        ["N", "R", "G", "P"],
        ["J", "T", "B", "L", "F", "G", "D", "C"],
        ["M", "S", "V"],
        ["L", "S", "R", "C", "Z", "P"],
        ["P", "S", "L", "V", "C", "W", "D", "Q"],
        ["C", "T", "N", "W", "D", "M", "S"],
        ["H", "D", "G", "W", "P"],
        ["Z", "L", "P", "H", "S", "C", "M", "V"],
        ["R", "P", "F", "L", "W", "G", "Z"]
    ]

    # Read actions from input.txt
    with open("input.txt") as f:
        # read from line 11 onwards
        for line in f.readlines()[10:]:
            line = line.strip()
            # Split line (move X from X to X) into count, from, to
            line = line.split(" ")
            count, frm, to = int(line[1]), int(line[3]), int(line[5])
            tmp = []
            for i in range(count):
                tmp.append(stacks[frm - 1].pop())
            while tmp:
                stacks[to - 1].append(tmp.pop())
    
    res = ""
    for stack in stacks:
        res += stack[-1]
    
    print(res)

#part1()
part2()