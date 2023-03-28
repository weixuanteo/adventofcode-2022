import re
import heapq
from collections import deque, defaultdict

def parse_input(input):
    # [current valve, flow rate, [neighbouring valves]]
    data = []
    with open(input) as f:
        for line in f:
            flow_rate = re.findall(r'-?\d+', line)
            # extract all double captial letters
            valves = re.findall(r'[A-Z]{2}', line)
            data.append([valves[0], int(flow_rate[0]), valves[1:]])
    return data

def get_distances(graph):
    distances = {}
    for valve in graph:
        visited = set()
        q = deque([(valve, 0)])
        while q:
            for _ in range(len(q)):
                visited_valve, distance = q.popleft()
                visited.add(visited_valve)
                for next_valve in graph[visited_valve]["connections"]:
                    if next_valve not in visited:
                        if graph[next_valve]["flow_rate"] != 0 or graph[valve]["flow_rate"] != 0:
                            distances[(valve, next_valve)] = distance + 1
                        q.append((next_valve, distance + 1))
    return distances

def part1():
    data = parse_input("input.txt")
    valves = {}
    for d in data:
        valves[d[0]] = {"connections": d[2], "flow_rate": d[1]}
    distances = get_distances(valves)

    max_pressure = 0
    q = deque([("AA", 30, 0, set())])
    while q:
        valve, time_left, total_relief, open_valves = q.popleft()
        max_pressure = max(max_pressure, total_relief)
        for next_valve in valves.keys():
            if next_valve not in open_valves and valves[next_valve]["flow_rate"] > 0:
                time = time_left - distances[(valve, next_valve)] - 1
                if time < 1:
                    continue
                open_valves.add(next_valve)
                q.append((next_valve, time, total_relief + valves[next_valve]["flow_rate"] * time, open_valves.copy()))
                open_valves.remove(next_valve)

    print("(Part 1) Max pressure found:", max_pressure)

def part2():
    data = parse_input("input.txt")
    valves = {}
    for d in data:
        valves[d[0]] = {"connections": d[2], "flow_rate": d[1]}
    distances = get_distances(valves)

    max_pressure_paths = defaultdict(int)
    q = deque([("AA", 26, 0, set())])
    while q:
        valve, time_left, total_relief, open_valves = q.popleft()
        fixed_open_valves = frozenset(open_valves)
        max_pressure_paths[fixed_open_valves] = max(max_pressure_paths[fixed_open_valves], total_relief)
        for next_valve in valves.keys():
            if next_valve not in open_valves and valves[next_valve]["flow_rate"] > 0:
                time = time_left - distances[(valve, next_valve)] - 1
                if time < 1:
                    continue
                open_valves.add(next_valve)
                q.append((next_valve, time, total_relief + valves[next_valve]["flow_rate"] * time, open_valves.copy()))
                open_valves.remove(next_valve)

    max_pressure = 0
    max_pressure_paths = [(v, k) for k, v in max_pressure_paths.items()]
    max_pressure_paths.sort(reverse=True)
    for i, (pressure, paths) in enumerate(max_pressure_paths, start=1):
        for comp_pressure, comp_path in max_pressure_paths[i:]:
            if comp_pressure + pressure <= max_pressure:
                break
            if paths.isdisjoint(comp_path):
                max_pressure = max(max_pressure, comp_pressure + pressure)
                break

    print("(Part 2) Max pressure found:", max_pressure)

part1()
part2()
