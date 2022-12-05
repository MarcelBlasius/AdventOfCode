def create_stacks(path):
    stacks = []
    f = open(path, "r")
    count = 0
    for line in f.readlines():
        striped = line.strip("\n")
        if striped[1] == "1":
            break

        start = striped[:4]
        end = striped[4:]
        while len(start) != 0:
            if len(stacks) <= count:
                stacks.append([])

            if start[1] != " ":
                stacks[count].append(start[1])

            count += 1
            start = end[:4]
            end = end[4:]

        count = 0

    f.close()

    for entry in stacks:
        entry.reverse()

    return stacks


def read_moves(path):
    f = open(path, "r")
    moves = []
    read = False
    for line in f.readlines():
        striped = line.strip("\n")
        if len(striped) == 0:
            read = True
            continue

        if not read:
            continue

        split = striped.split(" ")
        moves.append([int(split[1]), int(split[3]), int(split[5])])

    f.close()
    return moves


def exercise_1(stacks, moves):
    for move in moves:
        for i in range(move[0]):
            pop = stacks[move[1] - 1].pop()
            stacks[move[2] - 1].append(pop)

    return get_result(stacks)


def exercise_2(stacks, moves):
    for move in moves:
        toMove = []
        for i in range(move[0]):
            if len(stacks[move[1] - 1]) > 0:
                pop = stacks[move[1] - 1].pop()
                toMove.append(pop)
        if len(toMove) > 0:
            toMove.reverse()
            stacks[move[2] - 1] += toMove

    return get_result(stacks)


def get_result(stacks):
    result = ""

    for stack in stacks:
        if len(stack) > 0:
            result += stack.pop()
    return result


if __name__ == "__main__":
    stacks = create_stacks("input")
    moves = read_moves("input")
    print("Exercise 1:", exercise_1(stacks, moves))
    print("Exercise 2:", exercise_2(create_stacks("input"), moves))
