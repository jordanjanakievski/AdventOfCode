# Read the input file
input_file = open("input.txt", "r")
lines = input_file.readlines()

# Create a 2D array to store the word search
word_search = []
for line in lines:
    word_search.append(list(line.strip()))

forwards = "XMAS"
backwards = "SAMX"

def part1():
    # Need to find the word XMAS in the word search
    # 1. Horizontal (forwards and backwards)
    # 2. Vertical (forwards and backwards)
    # 3. Diagonal (forwards and backwards)
    total = 0

    for row in word_search:
        total += search_horizontally(row)

    total += search_vertically()
    total += search_diagonally()

    return total

def part2():
    total = 0

    total += look_for_A()

    return total

def search_horizontally(row):
    return ''.join(row).count(forwards) + ''.join(row).count(backwards)

def search_vertically():
    count = 0
    for i in range(len(word_search[0])):
        column = [row[i] for row in word_search]
        count += search_horizontally(column)
    return count

def search_diagonally():
    count = 0
    n = len(word_search)
    m = len(word_search[0])

    # Search diagonals from top-left to bottom-right
    for d in range(n + m - 1):
        diag1 = []
        diag2 = []
        for i in range(max(0, d - m + 1), min(n, d + 1)):
            diag1.append(word_search[i][d - i])
            diag2.append(word_search[i][m - 1 - (d - i)])
        count += ''.join(diag1).count(forwards)
        count += ''.join(diag2).count(forwards)
        count += ''.join(diag1).count(backwards)
        count += ''.join(diag2).count(backwards)

    return count


def look_for_A():
    total = 0
    for r in range(1, len(word_search) - 1):
        for c in range(1, len(word_search[0]) - 1):
            if word_search[r][c] == "A":
                # M _ M
                # _ A _
                # S _ S
                if word_search[r - 1][c - 1] == "M" and word_search[r - 1][c + 1] == "M" and word_search[r + 1][c - 1] == "S" and word_search[r + 1][c + 1] == "S":
                    total += 1
                
                # M _ S
                # _ A _
                # M _ S
                if word_search[r - 1][c - 1] == "M" and word_search[r - 1][c + 1] == "S" and word_search[r + 1][c - 1] == "M" and word_search[r + 1][c + 1] == "S":
                    total += 1

                # S _ S
                # _ A _
                # M _ M
                if word_search[r - 1][c - 1] == "S" and word_search[r - 1][c + 1] == "S" and word_search[r + 1][c - 1] == "M" and word_search[r + 1][c + 1] == "M":
                    total += 1

                # S _ M
                # _ A _
                # S _ M
                if word_search[r - 1][c - 1] == "S" and word_search[r - 1][c + 1] == "M" and word_search[r + 1][c - 1] == "S" and word_search[r + 1][c + 1] == "M":
                    total += 1
    return total



if __name__ == "__main__":
    print(part1())
    print(part2())
