with open("input.txt", 'r') as file:
    lines = file.readlines()
lines = [line.strip() for line in lines]

directions = {
    "L": -1,
    "R": 1
}

# Count the number of times the dial lands on 0
def part1():

    counter = 0
    position = 50

    for line in lines:
        direction = line[0]
        distance = int(line[1:])

        steps = (directions[direction] * distance) + position

        position = steps % 100

        if position == 0:
            counter += 1

    print("PART 1 RESULT: " + str(counter))

# Count the number of times the dial passes 0
def part2():

    counter = 0
    position = 50

    for line in lines:
        direction = line[0]
        distance = int(line[1:])

        distance_to_zero = position if direction == "L" else (100 - position) % 100

        # if we start at 0
        if distance_to_zero == 0:
            distance_to_zero = 100

        # completing at least one revolution
        if distance >= distance_to_zero:
            counter += 1 + (distance - distance_to_zero) // 100

        steps = (directions[direction] * distance) + position
        position = steps % 100

    print("PART 2 RESULT: " + str(counter))

if __name__ == "__main__":
    part1()
    part2()
