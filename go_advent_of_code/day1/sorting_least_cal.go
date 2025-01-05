package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"slices"
	"strconv"
	"strings"
	"math"
)

func test() {
	left_list := make([]string, 0)
	right_list := make([]string, 0)

	file, err := os.Open("./advent_day1.txt")

	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	// optionally, resize scanner's capacity for lines over 64K, see next example
	for scanner.Scan() {
		word := scanner.Text()
		words := strings.Split(word, "   ")
		left_list = append(left_list, words[0])
		right_list = append(right_list, words[1])

		// fmt.Println(scanner.Text())
	}
	slices.Sort(left_list)
	slices.Sort(right_list)
	fmt.Println(right_list)

	sum_of_difference := 0
	counter := 0
	for counter < len(left_list) {
		left_val, err := strconv.Atoi(left_list[counter])
		fmt.Println(left_val)
		if err != nil {
			// ... handle error
			panic(err)
		}
		right_val, err := strconv.Atoi(right_list[counter])
		fmt.Println(right_val)

		if err!=nil{
			panic(err)
		}
		sum_of_difference=sum_of_difference+int(math.Abs(float64(right_val)-float64(left_val)))
		counter = counter + 1
	}
	fmt.Println("the value of the sum is ", sum_of_difference)
	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}
}
