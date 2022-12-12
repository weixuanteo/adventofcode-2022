from collections import deque

def part1():
    grid = []
    with open('input.txt') as f:
        for line in f:
            grid.append(list(line.strip()))
    
    def get_elevation(a, b):
        if a == 'S' or (a == 'z' and b == 'E'):
            return 0
        if b == 'E':
            return 2
        return ord(b) - ord(a)
    
    directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

    start_pos = None
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 'S':
                start_pos = (i, j)
                break

    # BFS to find the shortest path to E
    q = deque()
    q.append((start_pos, 0, []))
    visited = set()
    rows, cols = len(grid), len(grid[0])
    while q:
        pos, steps, path = q.popleft()
        if pos in visited:
            continue
        visited.add(pos)
        x, y = pos
        path.append([pos, grid[x][y]])
       
        if grid[x][y] == 'E':
            print("Total steps:", steps)
            print("Path:", path)
            break
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if nx in range(rows) and ny in range(cols) and get_elevation(grid[x][y], grid[nx][ny]) < 2 and (nx, ny) not in visited:
                q.append(((nx, ny), steps + 1, path.copy()))

def part2():
    grid = []
    with open('input.txt') as f:
        for line in f:
            grid.append(list(line.strip()))
    
    def get_elevation(a, b):
        if a == 'S' or (a == 'z' and b == 'E'):
            return 0
        if b == 'E':
            return 2
        return ord(b) - ord(a)
    
    directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

    start_pos = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 'a':
                start_pos.append((i, j))

    # BFS to find the shortest path to E
    min_steps = float('inf')
    for start in start_pos:
        q = deque()
        q.append((start, 0, []))
        visited = set()
        rows, cols = len(grid), len(grid[0])
        while q:
            pos, steps, path = q.popleft()
            if pos in visited:
                continue
            visited.add(pos)
            x, y = pos
            path.append([pos, grid[x][y]])
        
            if grid[x][y] == 'E':
                # print("Total steps:", steps)
                # print("Path:", path)
                min_steps = min(min_steps, steps)
                break
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if nx in range(rows) and ny in range(cols) and get_elevation(grid[x][y], grid[nx][ny]) < 2 and (nx, ny) not in visited:
                    q.append(((nx, ny), steps + 1, path.copy()))
    print("Min steps:", min_steps)

part1()
part2()