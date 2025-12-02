with open("input.txt", 'r') as file:
    lines = file.readlines()
lines = [line.strip() for line in lines]
id_ranges = lines[0].split(',')

def part1():

    id_sum = 0

    for id_range in id_ranges:
        ids = id_range.split('-')
        start = int(ids[0])
        end = int(ids[1])

        # check if any id in the range has a repeat pattern
        # even len and looks like 123123, 55, 4040, etc
        for i in range(start, end + 1):

            istr = str(i)

            if len(istr) % 2 != 0:
                continue
            else:
                h = len(istr) //2
                id_sum += i if istr[:h] == istr[h:] else 0


    print("PART 1 RESULT: " + str(id_sum))

def part2():
    
    id_sum = 0

    for id_range in id_ranges:
        ids = id_range.split('-')
        start = int(ids[0])
        end = int(ids[1])

        # check if any id in the range has a repeat pattern
        # looks like 123123, 55, 4040, 111, 123123123
        for i in range(start, end + 1):

            istr = str(i)
            
            for c in range(1, len(istr)):
                length = len(istr)

                if istr[:c] * (length // c) == istr:
                    id_sum += i
                    break

    print("PART 2 RESULT: " + str(id_sum))

if __name__ == "__main__":
    part1()
    part2()
