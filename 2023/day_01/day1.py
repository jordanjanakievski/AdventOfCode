NUMBERS = {"one": 1, "two": 2, "three": 4, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9, "zero": 0}

def check_for_int(char, line):
    if char.isdigit():
        return int(char)
    else:
        for num in NUMBERS:
            if line.startswith(num):
                return NUMBERS[num]

# Read through the input.txt file
result = 0
input_file = open("input.txt", "r")
# Read the lines from the input
lines = input_file.readlines()

for line in lines:
    for char in line:
        if char.isdigit():
            result += 10 * int(char)
            break
    for char in line[::-1]:
        if char.isdigit():
            result += int(char)
            break

print("Part 1: " + str(result))

# =================================================================

result = 0

for line in lines:
    for i, char in enumerate(line):
        num = check_for_int(char, line[i:])
        if num:
            result += 10 * num
            break
        
    for i in range(len(line) - 1, -1, -1):
        num = check_for_int(line[i], line[i:])
        if num:
            result += num
            break

print("Part 2: " + str(result))
