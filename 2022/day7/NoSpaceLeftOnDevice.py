from typing import List


def calculate_directory_size(rows: List[str], directory: str):
    sizes = {}
    currentDirectorySize = 0
    rowsUsed = 0
    skip = 0
    for index in range(len(rows)):
        rowsUsed += 1
        if skip > 0:
            skip -= 1
            continue

        row = rows[index]
        if row.startswith("$ ls") or row.startswith("dir"):
            # do nothing
            continue

        if row.startswith("$ cd .."):
            break

        if row.startswith("$ cd"):
            directory_name = row.split(" ")[2]
            result = calculate_directory_size(rows[index + 1:], directory_name)
            currentDirectorySize += result[0][directory_name]
            sizes = sizes | result[0]
            skip = result[1]
            continue

        split = row.split(" ")
        currentDirectorySize += int(split[0])

    sizes[directory] = currentDirectorySize
    print(sizes, rowsUsed)
    return (sizes, rowsUsed)


def read_input(path):
    rows = []
    f = open(path, "r")
    for line in f.readlines():
        rows.append(line.strip("\n"))
        f.close()
    return rows


if __name__ == "__main__":
    puzzle_input = read_input("input")
    directory_sizes = calculate_directory_size(puzzle_input, "all")
    print(directory_sizes)
    exercise_1 = 0
    for size in directory_sizes[0].values():
        if size <= 100000:
            exercise_1 += size

    print("Exercise 1", exercise_1)
