import re

def extract_points(input):
    sensors, beacons = [], []

    with open(input) as f:
        for line in f:
            points = re.findall(r'-?\d+', line)
            sensors.append((int(points[0]), int(points[1])))
            beacons.append((int(points[2]), int(points[3])))

    return sensors, beacons

def get_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

def part1():
    input = 'input.txt'
    y = 2000000
    sensors, beacons = extract_points(input)
    beacons_locations = set(beacons)

    min_X, max_X = min([x[0] for x in sensors]), max([x[0] for x in sensors])
    min_X, max_X = min(min_X, min([x[0] for x in beacons])), max(max_X, max([x[0] for x in beacons]))

    def get_positions_by_y(y):
        distances = []
        for i in range(len(sensors)):
            distances.append(get_distance(sensors[i][0], sensors[i][1], beacons[i][0], beacons[i][1]))
        max_dist = max(distances)
        
        count = 0
        for x in range(min_X - max_dist, max_X + max_dist + 1):
            for i in range(len(sensors)):
                if get_distance(x, y, sensors[i][0], sensors[i][1]) <= distances[i] \
                        and (x, y) not in beacons_locations:
                    count += 1
                    break

        return count

    print("No of positions that cannot contain a beacon:", get_positions_by_y(y))

def part2():
    input = 'input.txt'
    y = 4000000
    sensors, beacons = extract_points(input)

    distances = []
    for i in range(len(sensors)):
        distances.append(get_distance(sensors[i][0], sensors[i][1], beacons[i][0], beacons[i][1]))

    # Solution taken from https://www.reddit.com/r/adventofcode/comments/zmcn64/comment/j0b90nr/?utm_source=reddit&utm_medium=web2x&context=3
    # the intersection points will be the missing scanner location
    # ( (b-a)/2 , (a+b)/2 )

    a_coeff, b_coeff = [], []
    # Gradient 1 line
    # y = x + sy-sx+r+1
    # y = x + sy-sx-r-1
    # Gradient -1 line
    # y = -x + sx+sy+r+1
    # y = -x + sx+sy-r-1
    for i in range(len(sensors)):
        x1, y1 = sensors[i][0], sensors[i][1]
        r = distances[i]
        a_coeff.append(y1-x1+r+1)
        a_coeff.append(y1-x1-r-1)
        b_coeff.append(x1+y1+r+1)
        b_coeff.append(x1+y1-r-1)

    for a in a_coeff:
        for b in b_coeff:
            intersect = ((b-a)//2, (a+b)//2)
            if all(0 < p < y for p in intersect) and all(get_distance(intersect[0], intersect[1], sensors[i][0], sensors[i][1]) > distances[i] for i in range(len(sensors))):
                print("Intersection:", intersect)
                print("Tuning Frequency:", y * intersect[0] + intersect[1])
                break

# compute time to run 
import time
start_time = time.time()
part1()
print("--- %s seconds ---" % (time.time() - start_time))

start_time = time.time()
part2()
print("--- %s seconds ---" % (time.time() - start_time))
