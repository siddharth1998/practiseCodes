package main

import "fmt"

type array struct {
	size int
}

// TODO Creation 
// TODO Addition into array 
// TODO Deletion from an array
// TODO Search
// TODO Traverseing 

func(*array) inserter( ogArray *[]int,element int) *[]int{
	output:=append((*ogArray) [],element)
	return &output
}

func (*array) createer(size int) *[]int {
	slice := make([]int, size)
	return &slice
}

func main() {
	var y= array{10}
	x:=y.createer(10)
	fmt.Println(x)
	z:=y.inserter(x,3)
	fmt.Println(z)
}
