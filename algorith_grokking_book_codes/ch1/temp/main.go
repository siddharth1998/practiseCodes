package main

import "fmt"

func main(){
	var a [2] string
	// Declaring string type of variable 
	a[0]="Hello"
	a[1]="There"
	fmt.Println(a[0],a[1])
	fmt.Println(a)

	primes := [6]float64{2, 3, 5, 7, 11, 13}
	fmt.Printf("%f",primes[2])
}