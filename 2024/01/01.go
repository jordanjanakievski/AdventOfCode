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
	lines := []string{}
	col_1 := []int{}
	col_2 := []int{}
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
		line := strings.Split(scanner.Text(), "   ")
		num1, _ := strconv.Atoi(line[0])
		num2, _ := strconv.Atoi(line[1])
		col_1 = append(col_1, num1)
		col_2 = append(col_2, num2)
	}

	// Print the results from each part
	fmt.Println(part1(col_1, col_2))
	fmt.Println(part2(col_1, col_2))

	// Check for errors
	if err := scanner.Err(); err != nil {
		fmt.Println("Error reading file")
		return
	}
}

func part1(col_1 []int, col_2 []int) int {

	sort.Ints(col_1)
	sort.Ints(col_2)

	distances := []int{}

	for i := 0; i < len(col_1); i++ {
		distances = append(distances, int(math.Abs(float64(col_1[i]-col_2[i]))))
	}

	return sum(distances)
}

func part2(col_1 []int, col_2 []int) int {

	similarities := []int{}

	for i := 0; i < len(col_1); i++ {
		total := 0
		curr_num := col_1[i]
		for j := 0; j < len(col_2); j++ {
			if curr_num == col_2[j] {
				total += 1
			}
		}
		similarities = append(similarities, (total * curr_num))
	}

	return sum(similarities)
}

func sum(arr []int) int {
	total := 0
	for _, val := range arr {
		total += val
	}
	return total
}
