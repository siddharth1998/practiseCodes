package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

type number struct{
	number int
	occurence int 
}

func CountOccurence(list1 []string,list2 []string) map[string]int{
	dict :=make(map[string]int)

	for _,num1 := range list1{
		_,ok:=dict[num1]
		if (ok){
			// was already there
			continue
		}
		for _,num2 := range list2{
			if(num1==num2){
				dict[num1]++;
			}
		}
	}
	return dict
}

func main() {
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
	}
	data:=CountOccurence(left_list,right_list)
	fmt.Println(data)
	result:=0
	for key,val := range data{
		key_int,_:=strconv.Atoi(key)// the key converted to the 
		result=result+key_int*val
	}
	fmt.Println("Sum is ",result)
}
