from collections import deque

def part1():
    map = []
    with open("input.txt") as f:
        for line in f:
            map.append([ int(n) for n in line.strip()])
    visible = set()

    rows, cols = len(map), len(map[0])
    # search top to bottom
    for c in range(1, cols - 1):
        prev = map[0][c]
        for r in range(1, rows - 1):
            prev = max(prev, map[r - 1][c])
            if map[r][c] > prev:
                visible.add((r, c))

    # search bottom to top
    for c in range(1, cols - 1):
        prev = map[rows - 1][c]
        for r in range(rows - 2, -1, -1):
            prev = max(prev, map[r + 1][c])
            if map[r][c] > prev:
                visible.add((r, c))
    
    # search left to right
    for r in range(1, rows - 1):
        prev = map[r][0]
        for c in range(1, cols - 1):
            prev = max(prev, map[r][c - 1])
            if map[r][c] > prev:
                visible.add((r, c))
    
    # search right to left
    for r in range(1, rows - 1):
        prev = map[r][cols - 1]
        for c in range(cols - 2, 0, -1):
            prev = max(prev, map[r][c + 1])
            if map[r][c] > prev:
                visible.add((r, c))

    print(len(visible) + rows * 2 + cols * 2 - 4)

part1()