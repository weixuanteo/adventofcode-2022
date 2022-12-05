# Parse input.txt

import heapq

def part1():
    max_calories = float('-inf')
    with open('input.txt') as f:
        total = 0
        for line in f:
            if line == '\n':
                max_calories = max(max_calories, total)
                total = 0
            else:
                total += int(line)
    print(max_calories)

def part2():
    heap = []
    with open('input.txt') as f:
        total = 0
        for line in f:
            if line == '\n':
                heapq.heappush(heap, -total)
                total = 0
            else:
                total += int(line)
        heapq.heappush(heap, -total)

    # Get the 3 largest values from the heap
    top_three = [-1 * heapq.heappop(heap) for _ in range(3)]
    print(sum(top_three))

# part1()
part2()