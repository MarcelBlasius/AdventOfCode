def read_input(path):
    f = open(path, "r")
    rounds = []
    for line in f.readlines():
        striped = line.strip("\n")
        rounds.append(striped.split(" "))

    f.close()
    return rounds


def item_score(item):
    if item == "A":
        return 1
    if item == "B":
        return 2
    if item == "C":
        return 3


def evaluate_round(item_a, item_b):
    if item_a == item_b:
        return 3

    if item_a == "A" and item_b == "B":
        return 6

    if item_a == "A" and item_b == "C":
        return 0

    if item_a == "B" and item_b == "A":
        return 0

    if item_a == "B" and item_b == "C":
        return 6

    if item_a == "C" and item_b == "A":
        return 6

    if item_a == "C" and item_b == "B":
        return 0


def win(item_a):
    if item_a == "A":
        return "B"

    if item_a == "B":
        return "C"

    if item_a == "C":
        return "A"


def draw(item_a):
    return item_a


def loose(item_a):
    if item_a == "A":
        return "C"

    if item_a == "B":
        return "A"

    if item_a == "C":
        return "B"


def exercise_1(rounds):
    totalscore = 0
    for round in rounds:
        transformed_b = chr(ord(round[1]) - 23)
        totalscore += item_score(transformed_b) + evaluate_round(round[0], transformed_b)

    return totalscore


def exercise_2(rounds):
    totalscore = 0
    for round in rounds:
        item = ""
        if round[1] == "X":
            item = loose(round[0])

        if round[1] == "Y":
            item = draw(round[0])

        if round[1] == "Z":
            item = win(round[0])

        totalscore += item_score(item) + evaluate_round(round[0], item)

    return totalscore


if __name__ == "__main__":
    puzzle_input = read_input("input")
    print("Exercise 1:", exercise_1(puzzle_input))
    print("Exercise 2:", exercise_2(puzzle_input))

