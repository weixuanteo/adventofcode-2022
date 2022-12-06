from collections import Counter

def part1():
    with open("input.txt") as f:
        stream = f.readline()
        marker = Counter(stream[:4])
        
        if len(marker) == 4:
            print(4)
            return
        
        i, j = 0, 3        
        while j < len(stream):
            marker[stream[i]] -= 1
            if marker[stream[i]] == 0:
                del marker[stream[i]]
            i += 1
            j += 1
            marker[stream[j]] = marker.get(stream[j], 0) + 1

            if len(marker) == 4:
                print(j + 1)
                return

def part2():
    with open("input.txt") as f:
        stream = f.readline()
        marker = Counter(stream[:14])
        
        if len(marker) == 14:
            print(14)
            return
        
        i, j = 0, 13        
        while j < len(stream):
            marker[stream[i]] -= 1
            if marker[stream[i]] == 0:
                del marker[stream[i]]
            i += 1
            j += 1
            marker[stream[j]] = marker.get(stream[j], 0) + 1

            if len(marker) == 14:
                print(j + 1)
                return

#part1()
part2()