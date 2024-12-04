def part1():
    calories = []
    with open('./input.txt') as f:
        lines = f.read().splitlines()
        total = 0
        for i in range(len(lines)):
            num = lines[i]
            if num == "":
                calories.append(total)
                total = 0
            else:
                total += int(num)
    return calories

def part2(calories: list[int]):
    return sorted(calories)[-3:]

if __name__ == "__main__":
    print(max(part1()))
    print(sum(part2(part1())))