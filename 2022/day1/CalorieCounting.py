def read_input(path):
    calories = []
    f = open(path, "r")

    current_calories = 0
    for line in f.readlines():
        striped = line.strip("\n")
        if len(striped) == 0:
            calories.append(current_calories)
            current_calories = 0
            continue

        current_calories += int(striped)

    calories.append(current_calories)
    f.close()
    return calories


def exercise_1(puzzle_input: [int]):
    return max(puzzle_input)


def exercise_2(puzzle_input: [int]):
    sorted_input = sorted(puzzle_input, reverse=True)[:3]
    return sum(sorted_input)


if __name__ == "__main__":
    puzzle_input = read_input("input")
    print("Exercise 1:", exercise_1(puzzle_input))
    print("Exercise 2:", exercise_2(puzzle_input))

