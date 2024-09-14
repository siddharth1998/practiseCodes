package main

import "fmt"

func createArray()*[3]int{
	array := new([3]int)
	return array
}

func delete(array *[3]int,index int)(status bool,element int){
	if index <3&& index>=0{
		popped_element:=array[index]
		array[index]=0
		return true,popped_element
	}else{
		return false,-1
	}

}

func insertIntoArray(array *[3]int,element int )(bool,int){
	// Assuming 0 is not allowed or 0 is empty
	if( element ==0){
		return false,-1
	}
	index:=-1
	for i :=range(array){
		if(array[i]==0){
			array[i]=element	
			index=i
			break
		}
	}
	if(index==-1){
		return false,-2
	}
	return true,index
	}

func searchElement(array *[3]int, element int)(index int){
	for index,val:= range(array){
		if val==element{
			return index
		}
	}
	return -1
}

func main(){
	var take_input int
	fmt.Println("Starting")
	array:=createArray()
	for index := range(array){
		fmt.Println(&array[index])
	}

	for i:=0; i<3; i++{
		
		fmt.Scanln(&take_input)
		status,y:=insertIntoArray(array,take_input)
		if status==false{
			if(y==-1){
				fmt.Println("Error,You gave 0 as input")
				break
			}
			if(y==-2){
				fmt.Println("Error, No space left in the array")
				break
			}
		}
	}
	status,pop:=delete(array,1)
	fmt.Printf("%t,  %d \n",status,pop)
	fmt.Println(array)
	fmt.Println(searchElement(array,10))
}

// return pointer means you can utilize the value 
// giving address 