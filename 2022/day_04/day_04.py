def part1():
    total = 0
    with open('./input.txt') as f:
        lines = f.read().splitlines()

        for line in lines:
            id_nums = line.split(',')
            first = id_nums[0].split('-')
            second = id_nums[1].split('-')

            if int(first[0]) <= int(second[0]) and int(first[1]) >= int(second[1]):
                total += 1
            elif int(second[0]) <= int(first[0]) and int(second[1]) >= int(first[1]):
                total += 1
            
    return total

def part2():
    total = 0
    with open('./input.txt') as f:
        lines = f.read().splitlines()

    for line in lines:
            id_nums = line.split(',')
            first = id_nums[0].split('-')
            second = id_nums[1].split('-')

            if int(second[0]) <= int(first[0]) <= int(second[1]):
                total += 1
            elif int(first[0]) <= int(second[0]) <= int(first[1]):
                total += 1
            
    return total

if __name__ == '__main__':
    print(part1())
    print(part2())