def part1():

     with open('./input.txt') as f:
        lines = f.read().splitlines()
        score = 0
        for i in range(len(lines)):

            if lines[i][0] == 'A' and lines[i][-1] == 'X':
                print('Tie')
                score += 3
                score += 1
            elif lines[i][0] == 'A' and lines[i][-1] == 'Y':
                print('Win')
                score += 6
                score += 2
            elif lines[i][0] == 'B' and lines[i][-1] == 'Y':
                print('Tie')
                score += 3
                score += 2
            elif lines[i][0] == 'B' and lines[i][-1] == 'Z':
                print('Win')
                score += 6
                score += 3
            elif lines[i][0] == 'C' and lines[i][-1] == 'Z':
                print('Tie')
                score += 3
                score += 3
            elif lines[i][0] == 'C' and lines[i][-1] == 'X':
                print('Win')
                score += 6
                score += 1
            else:
                if lines[i][-1] == 'X':
                    print('Loss')
                    score += 0
                    score += 1
                elif lines[i][-1] == 'Y':
                    print('Loss')
                    score += 0
                    score += 2
                elif lines[i][-1] == 'Z':
                    print('Loss')
                    score += 0
                    score += 3
        
        return score


def part2():
    with open('./input.txt') as f:
        lines = f.read().splitlines()
        score = 0
        for i in range(len(lines)):

            if lines[i][0] == 'A' and lines[i][-1] == 'X':
                print('Loss')
                score += 3
            elif lines[i][0] == 'A' and lines[i][-1] == 'Y':
                print('Tie')
                score += 3
                score += 1
            elif lines[i][0] == 'A' and lines[i][-1] == 'Z':
                print('Win')
                score += 6
                score += 2
            elif lines[i][0] == 'B' and lines[i][-1] == 'X':
                print('Loss')
                score += 1
            elif lines[i][0] == 'B' and lines[i][-1] == 'Y':
                print('Tie')
                score += 3
                score += 2
            elif lines[i][0] == 'B' and lines[i][-1] == 'Z':
                print('Win')
                score += 6
                score += 3
            elif lines[i][0] == 'C' and lines[i][-1] == 'X':
                print('Loss')
                score += 2
            elif lines[i][0] == 'C' and lines[i][-1] == 'Y':
                print('Tie')
                score += 3
                score += 3
            elif lines[i][0] == 'C' and lines[i][-1] == 'Z':
                print('Win')
                score += 6
                score += 1
        
        return score


if __name__ == '__main__':
    print(part1())
    print(part2())