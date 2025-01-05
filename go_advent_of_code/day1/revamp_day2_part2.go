//go:build day2_part2.go
// +build day2_part2.go

package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"strconv"
	"strings"
)

// difference calculates the absolute difference between two integers.
func difference(a, b int) int {
	return int(math.Abs(float64(a - b)))
}

// diffrule checks if the difference between two levels is valid (between 1 and 3).
func diffrule(a, b int) bool {
	diff := difference(a, b)
	return diff >= 1 && diff <= 3
}

// safe_or_not checks if the list follows the specified rules.
func safe_or_not(list1 []int) bool {
	if len(list1) < 2 {
		return true // Short sequences are trivially valid.
	}

	dampnerUsed := false
	asc := list1[0] < list1[1]
	prev := list1[0]

	for i := 1; i < len(list1); i++ {
		cur := list1[i]

		if !diffrule(prev, cur) {
			if dampnerUsed {
				return false // Already used a dampener, cannot skip again.
			}

			// Attempt to skip this level
			dampnerUsed = true
			if i+1 < len(list1) && diffrule(prev, list1[i+1]) {
				// Skip current level, update trend if valid
				if asc && prev > list1[i+1] || !asc && prev < list1[i+1] {
					return false
				}
				prev = list1[i+1]
				i++ // Skip next level
				continue
			} else {
				return false // Cannot skip to fix the sequence
			}
		}

		// Check trend consistency
		if asc && prev > cur || !asc && prev < cur {
			if dampnerUsed {
				return false // Invalid trend change after using a dampener.
			}

			// Attempt to skip this level
			dampnerUsed = true
			if i+1 < len(list1) && diffrule(prev, list1[i+1]) {
				if asc && prev > list1[i+1] || !asc && prev < list1[i+1] {
					return false
				}
				prev = list1[i+1]
				i++ // Skip next level
				continue
			} else {
				return false // Cannot skip to fix the trend
			}
		}

		prev = cur
	}

	return true
}


func main() {
	file, err := os.Open("./day2_advent_puzzle.txt")
	if err != nil {
		fmt.Println(err)
	}

	scanner := bufio.NewScanner(file)

	total_lines := 0
	count := 0
	for scanner.Scan() {
		total_lines++
		line := scanner.Text()
		list_words := strings.Split(line, " ")
		temp_list := make([]int, 0)
		for _, word := range list_words {
			conversion, _ := strconv.Atoi(word)
			temp_list = append(temp_list, conversion)

		}
		if safe_or_not(temp_list) {
			count++
		} else {
			fmt.Println("Wrong", temp_list)
		}

	}
	fmt.Println("the total safe ", count)
	fmt.Println("the total lines ", total_lines)

}
