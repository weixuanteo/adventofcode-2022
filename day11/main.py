import heapq
import math
class Monkey:
    def __init__(self, id, items=[], operation=[], test_divisor=1):
        self.id = id
        self.items = items
        self.operation = operation
        self.test_divisor = test_divisor
        self.true_monkey = None
        self.false_monkey = None
        self.inspects = 0

    def update(self, item):
        x, op, y = self.operation
        if y == "old":
            y = item
        if x == "old":
            x = item
        new = 0
        x, y = int(x), int(y)
        if op == "+":
            new = x + y
        elif op == "-":
            new =  x - y
        elif op == "*":
            new = x * y
        elif op == "/":
            new = x / y
        return new // 3

    def inspect(self):
        for i in range(len(self.items)):
            self.items[i] = self.update(self.items[i])
            if self.items[i] % self.test_divisor == 0:
                self.true_monkey.items.append(self.items[i])
            else:
                self.false_monkey.items.append(self.items[i])
            self.inspects += 1
        self.items = []
    
    def __str__(self):
        return f"Items: {self.items}\n" \
               f"Operation: {self.operation}\n" \
               f"Test Divisor: {self.test_divisor}\n" \
               f"True Monkey: {self.true_monkey.id}\n" \
               f"False Monkey: {self.false_monkey.id}"

class Monkey2(Monkey):
    def __init__(self, id, items=[], operation=[], test_divisor=1):
        super().__init__(id, items, operation, test_divisor)
        self.true_monkey = self
        self.false_monkey = self
        self.common_divisor = 0

    def update(self, item):
        x, op, y = self.operation
        if y == "old":
            y = item
        if x == "old":
            x = item
        new = 0
        x, y = int(x), int(y)
        if op == "+":
            new = x + y
        elif op == "-":
            new =  x - y
        elif op == "*":
            # prevent overflow that would not affect test divisors num
            new = (x * y) % self.common_divisor
        elif op == "/":
            new = x / y
        return new


def part1():
    lines = []
    with open("input.txt") as f:
        for line in f:
            line = line.strip()
            if line:
                lines.append(line)

    total_monkeys = len(lines) // 6
    monkeys = [Monkey(i) for i in range(total_monkeys)]
    ROUNDS = 20

    for i in range(0, len(lines), 6):
        # Get monkey id
        id = int(lines[i].split(" ")[1][0])
        # Get items
        items = lines[i+1].split(": ")[1].split(", ")
        items = [int(item) for item in items]
        # Get operation
        operation = lines[i+2].split(": ")[1].split("new = ")[1].split(" ")
        # Get test divisor
        divisor = int(lines[i+3].split("Test: divisible by ")[1])
        # Get true monkey
        true_id = int(lines[i+4].split("If true: throw to monkey ")[1])
        # Get false monkey
        false_id = int(lines[i+5].split("If false: throw to monkey ")[1])

        monkey = monkeys[id]
        monkey.items = items
        monkey.operation = operation
        monkey.test_divisor = divisor
        monkey.true_monkey = monkeys[true_id]
        monkey.false_monkey = monkeys[false_id]

    for i in range(ROUNDS):
        for monkey in monkeys:
            monkey.inspect()
        print(f"Round {i+1}")
        for id, monkey in enumerate(monkeys):
            print("Monkey", id, monkey.items)
        print()

    inspects = [-monkey.inspects for monkey in monkeys]
    heapq.heapify(inspects)
    top1 = -heapq.heappop(inspects)
    top2 = -heapq.heappop(inspects)
    print("Total Monkey Business:", top1 * top2)

def part2():
    lines = []
    with open("input.txt") as f:
        for line in f:
            line = line.strip()
            if line:
                lines.append(line)

    total_monkeys = len(lines) // 6
    monkeys = [Monkey2(i) for i in range(total_monkeys)]
    ROUNDS = 10000

    for i in range(0, len(lines), 6):
        # Get monkey id
        id = int(lines[i].split(" ")[1][0])
        # Get items
        items = lines[i+1].split(": ")[1].split(", ")
        items = [int(item) for item in items]
        # Get operation
        operation = lines[i+2].split(": ")[1].split("new = ")[1].split(" ")
        # Get test divisor
        divisor = int(lines[i+3].split("Test: divisible by ")[1])
        # Get true monkey
        true_id = int(lines[i+4].split("If true: throw to monkey ")[1])
        # Get false monkey
        false_id = int(lines[i+5].split("If false: throw to monkey ")[1])

        monkey = monkeys[id]
        monkey.items = items
        monkey.operation = operation
        monkey.test_divisor = divisor
        monkey.true_monkey = monkeys[true_id]
        monkey.false_monkey = monkeys[false_id]
    
    common_divisor = math.prod([monkey.test_divisor for monkey in monkeys])
    for monkey in monkeys:
        monkey.common_divisor = common_divisor

    for i in range(ROUNDS):
        for monkey in monkeys:
            monkey.inspect()
        print(f"Round {i+1}")
        # for id, monkey in enumerate(monkeys):
        #     print("Monkey", id, monkey.items)
        # print()

    inspects = [-monkey.inspects for monkey in monkeys]
    heapq.heapify(inspects)
    top1 = -heapq.heappop(inspects)
    top2 = -heapq.heappop(inspects)
    print("Total Monkey Business:", top1 * top2)
    
part1()
part2()