with open("input.txt", 'r') as file:
    lines = file.readlines()
lines = [line.strip() for line in lines]

def part1():

    result = 0

    for line in lines:
        l, r = 0, 0

        max_l = 0
        max_r = 0

        while r < len(line):

            if int(line[r]) > max_l and r != len(line) - 1:
                max_l = int(line[r])
                max_r = 0
                l = r
            
            if r > l and int(line[r]) > max_r:
                max_r = int(line[r])

            r += 1
        
        result += max_l * 10 + max_r

    print("PART 1 RESULT: " + str(result))

def part2():
    
    result = 0

    for line in lines:
        
        tracker = []

        for i in range(len(line)):
            tracker.append(line[i])

            if len(tracker) > 12:
                # remove the smallest value bit starting from left
                for j in range(len(tracker) - 1):
                    if int(tracker[j]) < int(tracker[j + 1]):
                        tracker.pop(j)
                        break
            
            # if nothing was removed, pop the most recent
            if len(tracker) > 12:
                tracker.pop()

        result += int("".join(tracker))
        
    print("PART 2 RESULT: " + str(result))


if __name__ == "__main__":
    part1()
    part2()
