package main

import (
	"fmt"
	"math"
)

func create()[]int{
	var data =make([]int,3)
	return data
}
// playing with slices

func double(array []int)[]int{
	new_array:=make([]int,len(array)*2)
	for i:=0;i<len(array);i++{
		new_array[i]=array[i]
	}
	return new_array
}

func insert(array []int,ele int)[]int{
	counter:=0
	for(counter<len(array)){
		if(array[counter]==0){
			array[counter]=ele
			return array
		}
		counter++
		
	}
	// No space left double the size of the array and insert
	new_array:=double(array)
	new_array[counter]=ele
	return new_array
}

func half_array(array []int)[]int{
	newLength:=math.Floor(float64(len(array))/float64(2.0))
	new_array:=make([]int,int64(newLength))
	for i:=0;i<len(array);i++{
		if array[i]==0{
			break
		}
		new_array[i]=array[i]
	}
	return new_array
}

func delete(array []int,index int)[]int{
	
	if(index>len(array) && index < 0){
		return array
	}
	var counter=index
	for(counter<len(array)-1){
		array[counter]=array[counter+1]
		counter++
	}
	array[counter]=0
	counter=0
	for counter< len(array){
		if array[counter]==0{
			break
		}
		counter++
	}
	if counter<= int(math.Floor(float64(len(array))/float64(2.0))){
		array=half_array(array)
	}
	return array
}

func main(){
	var array=create()
	fmt.Println(array)
	array=insert(array,1)
	array=insert(array,2)
	array=insert(array,3)
	array=insert(array,4)
	array=insert(array,5)
	array=insert(array,6)
	array=insert(array,7)
	array=insert(array,8)
	fmt.Println(array)
	fmt.Printf(" Size %d ",len(array))

	array=delete(array,4)
	array=delete(array,4)
	
	array=delete(array,4)
	fmt.Println(array)
	
	array=delete(array,2)
	fmt.Println("Decrease array",array)
	fmt.Printf(" Size %d ",len(array))
}