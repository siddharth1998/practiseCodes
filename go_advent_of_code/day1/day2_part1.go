//go:build day2_part1.go
// +build day2_part1.go

package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
	"strconv"
	"math"
)

func difference(a int, b int)float64{
	return math.Abs(float64(a-b))
}

func safe_or_not( list1 []int )bool{
	// The levels are either all increasing or all decreasing.
	// Any two adjacent levels differ by at least one and at most three.
	length:= len(list1)
	if length ==1{
		return true
	}else if length==2{
		diff:= difference(list1[0],list1[1])
		if diff < 1 ||  diff > 3{
			return false
		}else{
			return true
		}
	}else{
		asc:=false
		if list1[0]>list1[1]{
			asc=false
		}else if list1[0] < list1[1]{
			asc=true
		}else{
			return false
		}
		prev:=list1[0];
		for index,integer := range list1{
			if index>0{
				if asc{
					// Ascending
					if prev > integer{
						// property of descending 
						fmt.Println("Reejcted due to desscending in asc based series", prev, integer)
						return false
					}else{
						if difference(prev,integer) <1 || difference(prev,integer) >3{
							fmt.Println("Wrong the difference is ", difference(prev,integer), "in asc")

							return false
						}
					}
					
				}else{
					// Descending
					if prev < integer{
						fmt.Println("Reejcted due to asceding in dsc based series", prev, integer)

						return false
					}else{
						if difference(prev,integer) <1 || difference(prev,integer) >3{
							fmt.Println("Wrong the difference is ", difference(prev,integer), "in desc")
							return false
						}
					}
				}
				prev=integer
			}

		}
	}
	return true
}

func main() {
	file,err := os.Open("./day2_advent_puzzle.txt")
	if (err!=nil){
		fmt.Println(err)
	}

	scanner := bufio.NewScanner(file);

	total_lines:=0
	count :=0;
	for scanner.Scan(){
		total_lines++;
		line := scanner.Text()
		list_words := strings.Split(line," ")
		temp_list:= make([]int,0);
		for _,word := range list_words{
			conversion,_ :=strconv.Atoi(word)
			temp_list = append(temp_list, conversion )
			
		}
		if safe_or_not(temp_list){
			count++
		}
		
	}
	fmt.Println("the total safe ",count)
	fmt.Println("the total lines ",total_lines)

}
