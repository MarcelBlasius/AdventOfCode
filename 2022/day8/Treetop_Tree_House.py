def read_input(path):
    rows = []

    f = open(path, "r")
    for line in f.readlines():
        striped = line.strip("\n")
        rows.append([int(char) for char in striped])
        f.close()
    return rows


def visible_trees(rows):
    visible_trees = 0
    for rowIdx in range(len(rows)):
        if rowIdx == len(rows) - 1 or rowIdx == 0:
            visible_trees += len(rows[rowIdx])
            continue

        for entryIdx in range(len(rows[rowIdx])):
            if entryIdx == len(rows[rowIdx]) - 1 or entryIdx == 0:
                visible_trees += 1
                continue
            entry = rows[rowIdx][entryIdx]

            # look left
            tallest = True
            for tree in rows[rowIdx][0:entryIdx]:
                if tree >= entry:
                    tallest = False
                    break

            if tallest:
                visible_trees += 1
                continue

            # look right
            tallest = True
            for tree in rows[rowIdx][entryIdx + 1:]:
                if tree >= entry:
                    tallest = False
                    break

            if tallest:
                visible_trees += 1
                continue

            # look up
            tallest = True
            for i in range(rowIdx):
                if rows[i][entryIdx] >= entry:
                    tallest = False
                    break

            if tallest:
                visible_trees += 1
                continue

            # look down
            tallest = True
            for i in range(rowIdx + 1, len(rows)):
                if rows[i][entryIdx] >= entry:
                    tallest = False
                    break

            if tallest:
                visible_trees += 1
                continue

    return visible_trees


def highest_scenic_score(rows):
    scenic_score = 0
    for rowIdx in range(len(rows)):
        for entryIdx in range(len(rows[rowIdx])):
            entry = rows[rowIdx][entryIdx]

            # look left
            left_score = 0
            if entryIdx != 0:
                copy = rows[rowIdx][0:entryIdx]
                copy.reverse()
                for tree in copy:
                    left_score += 1
                    if tree >= entry:
                        break

            # look right
            right_score = 0
            if entryIdx != len(rows[rowIdx]) - 1:
                for tree in rows[rowIdx][entryIdx + 1:]:
                    right_score += 1
                    if tree >= entry:
                        break

            # look up
            up_score = 0
            if rowIdx != 0:
                current_row = rowIdx - 1
                while current_row != -1:
                    up_score += 1
                    if rows[current_row][entryIdx] >= entry:
                        break
                    current_row -= 1

            # look down
            down_score = 0
            if rowIdx != len(rows) - 1:
                for i in range(rowIdx + 1, len(rows)):
                    down_score += 1
                    if rows[i][entryIdx] >= entry:
                        break

            current_scenic_score = down_score * up_score * left_score * right_score
            if current_scenic_score > scenic_score:
                scenic_score = current_scenic_score

    return scenic_score


if __name__ == "__main__":
    rows = read_input("input")
    print("Exercise 1:", visible_trees(rows))
    print("Exercise 2:", highest_scenic_score(rows))

