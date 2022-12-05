def part1():
    shape_scores = {
        "X": 1,
        "Y": 2,
        "Z": 3,
    }
    scores = {
        "A-X": 3,
        "A-Y": 6,
        "A-Z": 0,
        "B-X": 0,
        "B-Y": 3,
        "B-Z": 6,
        "C-X": 6,
        "C-Y": 0,
        "C-Z": 3,
    }

    total = 0

    with open('input.txt') as f:
        for line in f:
            line = line.strip()
            opp, player = line.split(" ")
            total += scores[opp + "-" + player]
            total += shape_scores[player]
    print(total)

def part2():
    # X = lose
    # Y = draw
    # Z = win

    shape_scores = {
        "X": 1,
        "Y": 2,
        "Z": 3,
    }

    scores = {
        "A-X": 3,
        "A-Y": 6,
        "A-Z": 0,
        "B-X": 0,
        "B-Y": 3,
        "B-Z": 6,
        "C-X": 6,
        "C-Y": 0,
        "C-Z": 3,
    }

    choices = {
        "A-X": "Z",
        "A-Y": "X",
        "A-Z": "Y",
        "B-X": "X",
        "B-Y": "Y",
        "B-Z": "Z",
        "C-X": "Y",
        "C-Y": "Z",
        "C-Z": "X",
    }

    total = 0

    with open('input.txt') as f:
        for line in f:
            line = line.strip()
            opp, outcome = line.split(" ")
            # get choice for player
            choice = choices[opp + "-" + outcome]
            total += scores[opp + "-" + choice]
            total += shape_scores[choice]
    print(total)

#part1()
part2()