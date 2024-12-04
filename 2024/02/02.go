package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"sort"
	"strconv"
	"strings"
)

func main() {
	// Read the input file
	file, err := os.Open("input.txt")
	if err != nil {
		fmt.Println("Error reading file")
		return
	}
	defer file.Close()

	// Parse the input file
	var lines [][]int
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := scanner.Text()
		stringNumbers := strings.Fields(line)
		var numbers []int
		for _, stringNumber := range stringNumbers {
			number, _ := strconv.Atoi(stringNumber)
			numbers = append(numbers, number)
		}
		lines = append(lines, numbers)
	}

	fmt.Println(part1(lines))
	fmt.Println(part2(lines))
}

func part1(lines [][]int) int {
	safe_reports := 0
	for i := 0; i < len(lines); i++ {
		if is_ascending_or_descending(lines[i]) && is_within_bounds(lines[i]) {
			safe_reports += 1
		}
	}
	return safe_reports
}

func part2(lines [][]int) int {
	var unsafe_reports [][]int
	safe_reports := 0

	for _, row := range lines {
		if !is_ascending_or_descending(row) || !is_within_bounds(row) {
			unsafe_reports = append(unsafe_reports, row)
		} else {
			safe_reports += 1
		}
	}

	// An unsafe report can actually be safe if one number can be removed
	for _, row := range unsafe_reports {
		for i := 0; i < len(row); i++ {
			new_row := make([]int, len(row))
			copy(new_row, row)
			new_row = append(new_row[:i], new_row[i+1:]...)
			if is_ascending_or_descending(new_row) && is_within_bounds(new_row) {
				safe_reports += 1
				break
			}
		}
	}

	return safe_reports
}

func is_ascending_or_descending(row []int) bool {
	sorted_row := make([]int, len(row))
	copy(sorted_row, row)
	sort.Ints(sorted_row)

	reversed_row := make([]int, len(row))
	copy(reversed_row, row)
	sort.Sort(sort.Reverse(sort.IntSlice(reversed_row)))

	return equal(row, sorted_row) || equal(row, reversed_row)
}

func is_within_bounds(row []int) bool {
	for i := 0; i < len(row)-1; i++ {
		if math.Abs(float64(row[i]-row[i+1])) > 3 || math.Abs(float64(row[i]-row[i+1])) < 1 {
			return false
		}
	}
	return true
}

func reverseArray(arr []int) []int {
	n := len(arr)
	reversed := make([]int, n)
	for i := 0; i < n; i++ {
		reversed[i] = arr[n-1-i]
	}
	return reversed
}

func equal(a, b []int) bool {
	if len(a) != len(b) {
		return false
	}
	for i := range a {
		if a[i] != b[i] {
			return false
		}
	}
	return true
}
