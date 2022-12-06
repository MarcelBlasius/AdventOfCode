def find_distinct_characters(path, length):
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

    return -1


if __name__ == "__main__":
    print("Exercise 1:", find_distinct_characters("input", 4))
    print("Exercise 2:", find_distinct_characters("input", 14))


