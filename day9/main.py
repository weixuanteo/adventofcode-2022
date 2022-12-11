# Part 1 movement rules
# H and T must always be touching 
# T move one step in the direction of H if H is two steps directly ahead of T
# If H and T are not touching, not in the same row or column, T moves one step diagonally towards H

class Knot:
    def __init__(self, location=(0,0)):
        self.location = location

def is_same_row_col(loc1, loc2):
    x1, y1 = loc1
    x2, y2 = loc2
    return x1 == x2 or y1 == y2

def get_steps(loc1, loc2):
    # (1,1) (2,2) -> 1
    # (1,1) (3,2) -> 2
    # (1,1) (1, 3) -> 2
    # (1,2) (2,1) -> 2 
    if is_same_row_col(loc1, loc2):
        return abs(loc1[0]-loc2[0]) + abs(loc1[1]-loc2[1])
    return abs(loc1[0]-loc2[0]) + abs(loc1[1]-loc2[1]) - 1

def part1():
    head = Knot((0,0))
    tail = Knot((0,0))
    seen = {(0,0)}

    directions = {
        "R": (0,1),
        "L": (0,-1),
        "U": (1,0),
        "D": (-1,0)
    }

    motions = []
    with open("input.txt") as f:
        for line in f:
            line = line.strip().split(" ")
            direction, steps = line[0], int(line[1])
            motions.append((direction, steps))
    
    for direction, steps in motions:
        x, y = directions[direction]
        for _ in range(steps):
            nx, ny = head.location[0] + x, head.location[1] + y
            head.location = (nx, ny)
            # if head is two steps ahead of tail, move tail one step towards head
            if get_steps(head.location, tail.location) == 2 and is_same_row_col(head.location, tail.location):
                tail.location = (tail.location[0] + x, tail.location[1] + y)
                seen.add(tail.location)
            # if head and tail are not touching, move tail one step diagonally towards head
            elif get_steps(head.location, tail.location) == 2 and not is_same_row_col(head.location, tail.location):
                if head.location[0] > tail.location[0] and head.location[1] > tail.location[1]:
                    tail.location = (tail.location[0] + 1, tail.location[1] + 1)
                elif head.location[0] > tail.location[0] and head.location[1] < tail.location[1]:
                    tail.location = (tail.location[0] + 1, tail.location[1] - 1)
                elif head.location[0] < tail.location[0] and head.location[1] > tail.location[1]:
                    tail.location = (tail.location[0] - 1, tail.location[1] + 1)
                else:
                    tail.location = (tail.location[0] - 1, tail.location[1] - 1)
                seen.add(tail.location)
    print(len(seen))

class Head(Knot):
    def step(self, direction):
        # move 1 step in the direction
        x, y = self.location
        match direction:
            case 'U':
                y += 1
            case 'D':
                y -= 1
            case 'L':
                x -= 1
            case 'R':
                x += 1
        self.location = (x, y)


class Tail(Knot):
    def __init__(self):
        super().__init__()
        self.history = set()

    def follow(self, pos):
        x, y = pos
        cx, cy = self.location
        dist_x = x - cx
        dist_y = y - cy
        if abs(dist_x) == 2 and not dist_y: # horizontal
            xv = 1 if dist_x > 0 else -1
            cx += xv
        elif abs(dist_y) == 2 and not dist_x: # vertical
            yv = 1 if dist_y > 0 else -1
            cy += yv
        elif (abs(dist_y) == 2 and abs(dist_x) in (1, 2)) or (abs(dist_x) == 2 and abs(dist_y) in (1, 2)):
            xv = 1 if dist_x > 0 else -1
            cx += xv
            yv = 1 if dist_y > 0 else -1
            cy += yv
        self.location = (cx, cy)
        self.history.add((cx, cy))

def part2():
    # Solution for part 2 taken from Reddit AOC Day 9 solution
    head = Head()
    tails = [Tail() for _ in range(9)]
    
    motions = []
    with open("test2.txt") as f:
        for line in f:
            line = line.strip().split(" ")
            direction, steps = line[0], int(line[1])
            motions.append((direction, steps))

    for direction, steps in motions:
        for _ in range(steps):
            head.step(direction)
            tails[0].follow(head.location)
            for i in range(1, 9):
                tails[i].follow(tails[i-1].location)

    print(len(tails[-1].history))
    
part1()
part2()