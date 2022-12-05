def part1():
    total = 0
    with open("input.txt") as f:
        for line in f:
            line = line.strip()
            a, b = line.split(",")
            a1, a2 = a.split("-")
            b1, b2 = b.split("-")
            a1, a2, b1, b2 = int(a1), int(a2), int(b1), int(b2)

            # Check if a1, a2 is in range of b1, b2
            # else check if b1, b2 is in range of a1, a2
            if a1 >= b1 and a2 <= b2:
                total += 1
            elif b1 >= a1 and b2 <= a2:
                total += 1
    print(total)

def part2():
    total = 0
    with open("input.txt") as f:
        for line in f:
            line = line.strip()
            a, b = line.split(",")
            a1, a2 = a.split("-")
            b1, b2 = b.split("-")
            a1, a2, b1, b2 = int(a1), int(a2), int(b1), int(b2)

            # Check if a1, a2 overlaps with b1, b2
            # else check if b1, b2 overlaps with a1, a2
            if a1 <= b1 and a2 >= b1:
                total += 1
            elif b1 <= a1 and b2 >= a1:
                total += 1
    print(total)

#part1()
part2()