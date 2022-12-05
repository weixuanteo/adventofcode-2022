def part1():
    with open("input.txt") as f:
        total = 0
        for line in f:
            line = line.strip()
            # Split the sentence into two parts by total length / 2
            comp1, comp2 = line[:len(line) // 2], line[len(line) // 2:]
            comp2_set = set(comp2)
            
            # uppercase A - Z is 27 - 52
            # lowercase a - z is 1 - 26

            for c in comp1:
                if c in comp2_set:
                    if c.islower():
                        total += ord(c) - ord('a') + 1
                    else:
                        total += ord(c) - ord('A') + 27
                    break
    print(total)

def part2():
    with open("input.txt") as f:
        total = 0
        i = 0
        common_set = set()
        for line in f:
            line = line.strip()
            if i == 0:
                common_set = set(line)
            else:
                common_set = common_set.intersection(set(line))
            i += 1
            if i == 3:
                c = common_set.pop()
                if c.islower():
                        total += ord(c) - ord('a') + 1
                else:
                        total += ord(c) - ord('A') + 27
                common_set = set()
                i = 0
    print(total)
#part1()
part2()