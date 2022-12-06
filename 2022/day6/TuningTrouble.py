def exercise_1(path, length):
    f = open(path, "r")
    counter = 0
    entries = []
    line = f.readline()
    f.close()

    for char in line:
        counter += 1

        if char in entries:
            while char != entries.pop(0):
                pass

        entries.append(char)

        if len(entries) == length:
            return counter
    return counter


if __name__ == "__main__":
    print("Exercise 1:", exercise_1("input", 4))
    print("Exercise 2:", exercise_1("input", 14))


