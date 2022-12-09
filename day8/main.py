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

def part2():
    map = []
    with open("input.txt") as f:
        for line in f:
            map.append([ int(n) for n in line.strip()])

    rows, cols = len(map), len(map[0])

    max_score = 0
    for r in range(rows):
        for c in range(cols):
            up, down, left, right = 0, 0, 0, 0
            prev = map[r][c]

            # search top to bottom (down)
            for i in range(r + 1, rows):
                down += 1
                if map[i][c] >= prev:
                    break
            
            # search bottom to top (up)
            for i in range(r - 1, -1, -1):
                up += 1
                if map[i][c] >= prev:
                    break
            
            # search left to right (right)
            for i in range(c + 1, cols):
                right += 1
                if map[r][i] >= prev:
                    break
            
            # search right to left (left)
            for i in range(c - 1, -1, -1):
                left += 1
                if map[r][i] >= prev:
                    break

            max_score = max(max_score, up * down * left * right)

    print(max_score)

part1()
part2()