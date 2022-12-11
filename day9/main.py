# Part 1 movement rules
# H and T must always be touching 
# T move one step in the direction of H if H is two steps directly ahead of T
# If H and T are not touching, not in the same row or column, T moves one step diagonally towards H

class Knot:
    def __init__(self, location):
        self.location = location

def is_same_row_col(loc1, loc2):
    x1, y1 = loc1
    x2, y2 = loc2
    return x1 == x2 or y1 == y2

def get_steps(loc1, loc2):
    # (1,1) (2,2) -> 1
    # (1,1) (3,2) -> 2
    # (1,1) (1, 3) -> 2
    # (1,2) (2,1) -> 1
 
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

part1()