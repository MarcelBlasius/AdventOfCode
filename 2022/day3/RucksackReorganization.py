def read_input(path):
    f = open(path, "r")
    rucksacks = []
    for line in f.readlines():
        striped = line.strip("\n")
        rucksacks.append([striped[:int(len(striped) / 2)], striped[int(len(striped) / 2):]])

    f.close()
    return rucksacks


def get_priority(item: str):
    if item.islower():
        return ord(item) - 96

    return ord(item) - 38


def exercise_1(puzzle_input):
    sum_priorities = 0

    for rucksack in puzzle_input:
        (comp_1, comp_2) = rucksack
        for item in comp_1:
            if item in comp_2:
                sum_priorities += get_priority(item)
                break

    return sum_priorities


def exercise_2(puzzle_input):
    sum_priorities = 0

    group = []
    for comp_1, comp_2 in puzzle_input:
        rucksack = comp_1 + comp_2
        group.append(rucksack)
        if len(group) == 3:
            for item in group[0]:
                if item in group[1] and item in group[2]:
                    sum_priorities += get_priority(item)
                    group = []
                    break

    return sum_priorities


if __name__ == "__main__":
    puzzle_input = read_input("input")
    print("Exercise 1:", exercise_1(puzzle_input))
    print("Exercise 2:", exercise_2(puzzle_input))

