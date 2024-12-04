# Read the input file
input_file = open("input.txt", "r")
lines = input_file.readlines()

lines = [line.strip().split() for line in lines]
lines = [[int(x) for x in pair] for pair in lines]
col_1 = [pair[0] for pair in lines]
col_2 = [pair[1] for pair in lines]


# Part 1
# Each line is set up like "123 456\n"
# Need to make a list of each column from the pairs of each line
def part1():
  col_1.sort()
  col_2.sort()

  distances = []

  for i in range(len(col_1)):
      x = col_1[i]
      y = col_2[i]
      distances.append(abs(x - y))

  return sum(distances)


# Part 2
# We will need to find how many times the number form col_1 appears in col_2
def part2():
  # iterate through col 1
  # find how many times num is in col 2

  similarity = []

  for num in col_1:
    total = col_2.count(num)
    similarity.append(total * num)

  return sum(similarity)



if __name__ == "__main__":
    print(part1())
    print(part2())