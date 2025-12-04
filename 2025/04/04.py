with open("input.txt", 'r') as file:
    lines = file.readlines()
lines = [list(line.strip()) for line in lines]

def part1():

    n = len(lines)
    m = len(lines[0])

    directions = [[1,0], [1,1], [1,-1], [0,1], [0,-1], [-1,0], [-1,1], [-1,-1]]
    def bfs(r, c):

        free_space = 0

        # check surrounding locations
        for direction in directions:
            nc, nr = direction[0] + c, direction[1] + r

            # check empty locations
            # off-grid or .
            if nc >= m or nr >= n or nc < 0 or nr < 0 or lines[nr][nc] == '.':
                free_space += 1

        if free_space >= 5:
            return 1
        return 0

    result = 0

    for r in range(n): # rows
        for c in range(m): # cols
            if lines[r][c] == '@':
                result += bfs(r, c)

    print("PART 1 RESULT: " + str(result))

def part2():

    n = len(lines)
    m = len(lines[0])

    directions = [[1,0], [1,1], [1,-1], [0,1], [0,-1], [-1,0], [-1,1], [-1,-1]]
    def bfs(r, c):

        free_space = 0

        # check surrounding locations
        for direction in directions:
            nc, nr = direction[0] + c, direction[1] + r

            # check empty locations
            # off-grid or .
            if nc >= m or nr >= n or nc < 0 or nr < 0 or lines[nr][nc] == '.':
                free_space += 1

        if free_space >= 5:
            lines[r][c] = '.'

            removed_units = 0

            for direction in directions:
                nc, nr = direction[0] + c, direction[1] + r

                # check empty locations
                # off-grid or .
                if nc >= m or nr >= n or nc < 0 or nr < 0 or lines[nr][nc] == '.':
                    continue
                else:
                    removed_units += bfs(nr, nc)

            return 1 + removed_units
        return 0

    result = 0

    for r in range(n): # rows
        for c in range(m): # cols
            if lines[r][c] == '@':
                result += bfs(r, c)

    print("PART 2 RESULT: " + str(result))

if __name__ == "__main__":
    part1()
    part2()
