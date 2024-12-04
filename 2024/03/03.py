import re

# Read the input file
input_file = open("input.txt", "r")
lines = input_file.readlines()

def part1():
    total = 0

    for line in lines:
        total += regex_mul_finder(line)

    return total


def part2():
    total = 0
    do = True
    for line in lines:
        occurrences = re.finditer(r"mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don\'t\(\)", line)
        for occurance in occurrences:
            if occurance.group() == "do()":
                do = True
            elif occurance.group() == "don't()":
                do = False
            elif do:
                total += regex_mul_finder(occurance.group())

    return total

def regex_mul_finder(line):
    sub_total = 0
    occurances = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", line)
    for occurance in occurances:
        sub_total += int(occurance[0]) * int(occurance[1])

    return sub_total

if __name__ == "__main__":
    print(part1())
    print(part2())
