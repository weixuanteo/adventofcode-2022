
def get_min_max_width_height(input):
    # Find the max height and width from the input to construct the environment
    max_height, max_width = 0, 0
    min_width = float('inf')
    with open(input) as f:
        for line in f:
            line = line.strip().split('->')
            for l in line:
                w,h = l.strip().split(',')
                w,h = int(w), int(h)
                max_width = max(max_width, w)
                max_height = max(max_height, h)
                min_width = min(min_width, w)
    return [max_height, max_width, min_width]

def construct_env(min_w, max_w, h):
    env = []
    for _ in range(h + 1):
        env.append(['.'] * (max_w - min_w + 1))
    return env

def print_env(env, min_w, max_w):
    widths = [str(i) for i in range(min_w, max_w + 1)]
    for i in range(3):
        print(' ' + ''.join([w[i] for w in widths]))
    for i, row in enumerate(env):
        print(str(i) + ''.join(row))

def construct_rocks(env, input, min_w):
    with open(input) as f:
        for line in f:
            line = line.strip().split('->')
            line = [l.strip().split(',') for l in line]
            i = 0
            while i < len(line) - 1:
                w1,h1 = int(line[i][0]), int(line[i][1])
                w2,h2 = int(line[i+1][0]), int(line[i+1][1])
                if h1 == h2:
                    if w2 < w1:
                        w1,w2 = w2,w1
                    for w in range(w1, w2 + 1):
                        env[h1][w - min_w] = '#'
                else:
                    if h2 < h1:
                        h1,h2 = h2,h1
                    for h in range(h1, h2 + 1):
                        env[h][w1 - min_w] = '#'
                i += 1
            
class Sand:
    def __init__(self, env, min_w):
        self.start = [500 - min_w, 0]
        self.env = env
        self.min_w = min_w
        self.current_pos = self.start
        self.is_abyss = False
    
    def can_go_down(self):
        if self.current_pos[1] + 1 < len(self.env) and self.env[self.current_pos[1] + 1][self.current_pos[0]] == '.':
            return True
        # abyss
        elif self.current_pos[1] + 1 >= len(self.env):
            self.is_abyss = True
            return True
        return False

    def go_down(self):
        self.current_pos[1] += 1

    def can_go_down_left(self):
        if (self.current_pos[0] - 1 >= 0 and 
            self.current_pos[1] + 1 < len(self.env) and
            self.env[self.current_pos[1] + 1][self.current_pos[0] - 1] == '.'):
            return True
        elif self.current_pos[0] - 1 < 0 or self.current_pos[1] + 1 >= len(self.env):
            self.is_abyss = True
            return True
        return False
    
    def go_down_left(self):
        self.current_pos[0] -= 1
        self.current_pos[1] += 1

    def can_go_down_right(self):
        if (self.current_pos[0] + 1 < self.min_w + len(self.env[0]) and 
            self.current_pos[1] + 1 < len(self.env) and 
            self.env[self.current_pos[1] + 1][self.current_pos[0] + 1] == '.'):
            return True
        elif self.current_pos[0] + 1 >= self.min_w + len(self.env[0]) or self.current_pos[1] + 1 >= len(self.env):
            self.is_abyss = True
            return True
        return False
    
    def go_down_right(self):
        self.current_pos[0] += 1
        self.current_pos[1] += 1

    def drop(self):
        while True:
            if self.is_abyss:
                break
            # try going down
            if self.can_go_down():
                self.go_down()
            # if can't go down, try going diagonally down left
            elif self.can_go_down_left():
                self.go_down_left()
            # if can't go diagonally down left, try going diagonally down right
            elif self.can_go_down_right():
                self.go_down_right()
            # if can't go diagonally down right, rest
            else:
                self.env[self.current_pos[1]][self.current_pos[0]] = 'o'
                break


def part1():
    input = 'input.txt'
    values = get_min_max_width_height(input)
    env = construct_env(values[2], values[1], values[0])
    print("Initial before adding rocks")
    print_env(env, values[2], values[1])
    construct_rocks(env, input, values[2])
    print("After adding rocks")
    print_env(env, values[2], values[1])
    print()

    i = 1
    while True:
        sand = Sand(env, values[2])
        sand.drop()
        if sand.is_abyss:
            print("Final state")
            print("===========")
            print_env(env, values[2], values[1])
            print("Abyss reached at sand {}".format(i))
            print("{} units of sand came to rest".format(i - 1))
            break
        i += 1
            

part1()
