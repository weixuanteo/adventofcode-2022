from collections import deque

class Node:
    def __init__(self, name="", is_dir=False):
        self.name = name
        self.is_dir = is_dir
        self.children = []
        self.size = 0
        self.parent = None

def create_tree():
    commands = []
    root = None
    with open("input.txt") as f:
        for line in f:
            commands.append(line.strip().split(" "))
    
    current = root
    for command in commands:
        if command[0] == '$' and command[1] == 'cd' and command[2] == '..':
            current = current.parent
        elif command[0] == '$' and command[1] == 'cd':
            if current is None:
                current = Node(command[2], True)
                root = current
            else:
                for child in current.children:
                    if child.name == command[2]:
                        current = child
                        break
        elif command[0] == 'dir':
            node = Node(command[1], True)
            node.parent = current
            current.children.append(node)
        elif command[0].isdigit():
            node = Node(command[1])
            node.size = int(command[0])
            node.parent = current
            current.children.append(node)
    return root

def part1():
    root = create_tree()

    total = 0
    # Recursive post order traversal, update size of each directory node, if size is at most 100000, add to the sum
    def dfs(node):
        nonlocal total
        if node.is_dir:
            for child in node.children:
                dfs(child)
                node.size += child.size
            if node.size <= 100000:
                total += node.size
    dfs(root)
    print(total)

def part2():
    root = create_tree()

    # Recursive post order traversal, update size of each directory node
    def dfs(node):
        if node.is_dir:
            for child in node.children:
                dfs(child)
                node.size += child.size
    dfs(root)
    
    MIN_DELETE_SPACE = root.size - (70000000 - 30000000)
    chosen_dir = float('inf')
    def preorder(node):
        nonlocal chosen_dir
        if node.size >= MIN_DELETE_SPACE:
            chosen_dir = min(chosen_dir, node.size)
        for child in node.children:
            preorder(child)
    
    preorder(root)
    print(chosen_dir)

part1()
part2()