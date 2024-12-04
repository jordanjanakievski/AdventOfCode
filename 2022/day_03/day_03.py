def part1():
    result = 0
    with open('./input.txt') as f:
        lines = f.read().splitlines()
        for line in lines:
            mid = len(line) // 2
            f = line[:mid]
            b = line[mid:]

            for i in range(len(f)):
                if f[i] in b:
                    if f[i].isupper():
                        result += ord(f[i]) - 64 + 26
                    else:
                        result += ord(f[i]) - 96
                    break
    return result

def part2():
    result = 0
    with open('./input.txt') as f:
        lines = f.read().splitlines()
        for i in range(0, len(lines) - 2, 3):
            line_1 = lines[i]
            line_2 = lines[i + 1]
            line_3 = lines[i + 2]

            for j in range(len(lines[i])):
                if line_1[j] in line_2 and line_1[j] in line_3:
                    if line_1[j].isupper():
                        result += ord(line_1[j]) - 64 + 26
                    else:
                        result += ord(line_1[j]) - 96
                    break
                
    return result

if __name__ == '__main__':
    print(part1())
    print(part2())