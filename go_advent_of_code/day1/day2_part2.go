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

func difference(a int, b int) float64 {
	return math.Abs(float64(a - b))
}

func safe_or_not(list1 []int) bool {
	// The levels are either all increasing or all decreasing.
	// Any two adjacent levels differ by at least one and at most three.
	dampner_used := false

	asc := false
	if list1[0] > list1[1] {
		asc = false
	} else {
		asc = true
	}
	flag:=false
	prev := list1[0]
	for index, integer := range list1 {
		if dampner_used == true && index<2 && list1[1] > list1[2] && flag==false{
			asc = false
			fmt.Println("Index false",index,list1);
			flag=true
		} else if dampner_used == true && index<2  && list1[1] < list1[2] && flag==false {
			asc = true
			flag=true
		} else if dampner_used == true && index<2 && list1[1] == list1[2] && flag==false {
			return false
		}

		if index > 0 {
			if asc {
				// Ascending
				if prev > integer {
					// property of descending
					if dampner_used {
						fmt.Println("Reejcted due to desscending in asc based series", prev, integer)
						return false
					} else {
						fmt.Println("Descending property", prev, integer, list1)

						dampner_used = true
						continue
					}
				} else {
					if difference(prev, integer) < 1 || difference(prev, integer) > 3 {
						if dampner_used {
							fmt.Println("Wrong the difference is ", difference(prev,integer), "in asc")
							return false
						} else {

							fmt.Println("Ascending property", prev, integer, list1)
							dampner_used = true
							continue
						}
					}
				}

			} else {
				// Descending
				if prev < integer {
					if dampner_used {
						fmt.Println("Reejcted due to asceding in dsc based series", prev, integer)

						return false
					} else {
						fmt.Println("Ascending continue",prev,integer)
						dampner_used = true
						continue
					}
				} else {
					if difference(prev, integer) < 1 || difference(prev, integer) > 3 {

						if dampner_used {
							fmt.Println("Wrong the difference is ", difference(prev,integer), "in desc")

							return false
						} else {
							fmt.Println("Descending continue",prev,integer)

							dampner_used = true
							continue
						}
					}
				}
			}
			prev = integer
		}

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
