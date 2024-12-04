# Read the input file
input_file = open("input.txt", "r")
lines = input_file.readlines()

lines = [line.strip().split() for line in lines]
lines = [[int(x) for x in line] for line in lines]

def part1():

  safe_reports = 0
  for row in lines:
    # Check the row for two conditions
    # 1. The row is all ascending or descending
    # 2. The difference between two numbers next to each other is not greater than 3 or less than 1
    # If both conditions are met, add 1 to the count
    if is_ascending_or_descending(row) and is_within_bounds(row):
      safe_reports += 1

  return safe_reports


def part2():

  unsafe_reports = []
  safe_reports = 0

  for row in lines:
    if not is_ascending_or_descending(row) or not is_within_bounds(row):
      unsafe_reports.append(row)
    else:
      safe_reports += 1

  # An unsafe report can actually be safe if one number can be removed
  for row in unsafe_reports:
    for i in range(len(row)):
      new_row = row.copy()
      new_row.pop(i)
      if is_ascending_or_descending(new_row) and is_within_bounds(new_row):
        safe_reports += 1
        break

  return safe_reports


def is_ascending_or_descending(row):
  return row == sorted(row) or row == sorted(row, reverse=True)

def is_within_bounds(row):
  for i in range(len(row) - 1):
    if abs(row[i] - row[i + 1]) > 3 or abs(row[i] - row[i + 1]) < 1:
      return False
  return True

if __name__ == "__main__":
    print(part1())
    print(part2())