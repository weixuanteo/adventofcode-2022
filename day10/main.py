def part1():
    instructions = []
    cycles = {20, 60, 100, 140, 180, 220}
    with open("input.txt") as f:
        for line in f:
            line = line.strip().split(" ")
            instructions.append(line)
    
    def check_cycle(x, cycle):
        if cycle in cycles:
            print("Cycle:", cycle, ":", x * cycle)
            return x * cycle
        return 0

    cycle, x = 0, 1
    i = 0
    sum = 0
    while i < len(instructions):
        inst = instructions[i][0]
        cycle += 1
        sum += check_cycle(x, cycle)
        if inst == "noop":
            i += 1
            continue
        cycle += 1 # 2nd cycle of addx
        sum += check_cycle(x, cycle)
        x += int(instructions[i][1])
        i += 1
    print(sum)

def part2():
    instructions = []
    with open("input.txt") as f:
        for line in f:
            line = line.strip().split(" ")
            instructions.append(line)
    
    crt = [[" " for _ in range(40)] for _ in range(6)]

    def render_crt():
        for row in crt:
            print("".join(row))

    cycle, x = 0, 1
    i = 0
    pos = 1
    while i < len(instructions):
        inst = instructions[i][0]
        cycle += 1
        
        if (cycle-1) % 40 in [pos - 1, pos, pos + 1]:
            crt[(cycle-1) // 40][(cycle-1) % 40] = "#"
        else:
            crt[(cycle-1) // 40][(cycle-1) % 40] = " "

        if inst == "noop":
            i += 1
            continue

        cycle += 1 # 2nd cycle of addx
        if (cycle-1) % 40 in [pos % 40 - 1, pos % 40, pos % 40 + 1]:
            crt[(cycle-1) // 40][(cycle-1) % 40] = "#"
        else:
            crt[(cycle-1) // 40][(cycle-1) % 40] = " "
        x += int(instructions[i][1])

        pos = x
        i += 1

    render_crt()
part1()
part2()