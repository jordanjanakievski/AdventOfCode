with open("input.txt", "r") as file:
    lines = file.readlines()
lines = [line.strip() for line in lines]

import math


def part1():
    result = 0

    nums: list[list[str]] = []

    for line in lines:
        numsSeq = line.split(" ")
        nums.append(numsSeq)

    for numSeq in nums:
        while "" in numSeq:
            numSeq.remove("")

    symbols = nums[-1]
    nums = nums[:-1]

    i = 0

    while i < len(nums[0]):
        if symbols[i] == "*":
            result += (
                int(nums[0][i]) * int(nums[1][i]) * int(nums[2][i]) * int(nums[3][i])
            )
        else:
            result += (
                int(nums[0][i]) + int(nums[1][i]) + int(nums[2][i]) + int(nums[3][i])
            )

        i += 1

    print("PART 1 RESULT: " + str(result))


def part2():
    result = 0

    symbols = lines[-1] + " "

    i = len(lines[0]) - 1
    lines[2] = " " + lines[2]
    lines[3] = "  " + lines[3]

    tracker: list[int] = []

    while i >= 0:
        if symbols[i] != " ":
            # perform the calc
            num = lines[0][i] + lines[1][i] + lines[2][i] + lines[3][i]
            tracker.append(int(num))
            if symbols[i] == "*":
                result += math.prod(tracker)
            else:
                result += sum(tracker)

            tracker = []
            i -= 1
        else:
            num = lines[0][i] + lines[1][i] + lines[2][i] + lines[3][i]
            tracker.append(int(num))

        i -= 1

    print("PART 2 RESULT: " + str(result))


if __name__ == "__main__":
    part1()
    part2()
