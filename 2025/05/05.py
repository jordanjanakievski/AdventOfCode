with open("input.txt", "r") as file:
    lines = file.readlines()
lines = [line.strip() for line in lines]


def part1():
    result = 0

    ingredients = False

    fresh: list[list[int]] = []

    for line in lines:
        if line == "":
            ingredients = True
            continue

        if not ingredients:
            ranges = line.split("-")
            fresh.append([int(ranges[0]), int(ranges[1])])

        else:
            ingredient = int(line)

            for pair in fresh:
                if pair[0] <= ingredient <= pair[1]:
                    result += 1
                    break

    print("PART 1 RESULT: " + str(result))


def part2():
    result = 0

    fresh: list[list[int]] = []

    for line in lines:
        if line == "":
            break

        ranges = line.split("-")
        fresh.append([int(ranges[0]), int(ranges[1])])

    fresh.sort()

    condensed: list[list[int]] = []

    for interval in fresh:
        start = interval[0]
        end = interval[1]

        if len(condensed) == 0:
            condensed.append([start, end])
            continue
        else:
            backStart = condensed[-1][0]
            backEnd = condensed[-1][1]

            if backStart <= start <= backEnd:
                condensed[-1][1] = max(backEnd, end)
            else:
                condensed.append([start, end])

    for item in condensed:
        result += item[1] - item[0] + 1

    print("PART 2 RESULT: " + str(result))


if __name__ == "__main__":
    part1()
    part2()
