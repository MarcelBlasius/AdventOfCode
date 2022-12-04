def read_input(path):
    f = open(path, "r")
    sections = []
    for line in f.readlines():
        striped = line.strip("\n")
        sections.append(striped.split(","))
    f.close()
    print(len(sections))
    return sections


def exercise_1(sections):
    overlaps = 0

    for elf_1, elf_2 in sections:
        split_1 = elf_1.split("-")
        split_2 = elf_2.split("-")
        if int(split_1[0]) >= int(split_2[0]) and int(split_1[1]) <= int(split_2[1]) or\
                int(split_2[0]) >= int(split_1[0]) and int(split_2[1]) <= int(split_1[1]):
            print(split_1, split_2)
            overlaps += 1

    return overlaps


def exercise_2(sections):
    overlaps = 0

    for elf_1, elf_2 in sections:
        split_1 = elf_1.split("-")
        split_2 = elf_2.split("-")
        range_1 = list(range(int(split_1[0]), int(split_1[1]) + 1))
        range_2 = list(range(int(split_2[0]), int(split_2[1]) + 1))

        for number in range_1:
            if number in range_2:
                overlaps += 1
                break

    return overlaps


if __name__ == "__main__":
    puzzle_input = read_input("input")
    print("Exercise 1:", exercise_1(puzzle_input))
    print("Exercise 2:", exercise_2(puzzle_input))
