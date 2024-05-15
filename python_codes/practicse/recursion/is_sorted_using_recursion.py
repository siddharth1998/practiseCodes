def isSorted(list_array:list[int],index:int=0)->bool:
    '''
    list_array: Input an interger array
    index: index from starting
    '''
    if index==len(list_array)-1:
        return True
    else:
        return list_array[index]<list_array[index+1] and isSorted(list_array,index+1)
    
print(isSorted([1,5,3,4],0))