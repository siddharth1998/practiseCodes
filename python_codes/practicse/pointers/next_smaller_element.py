def next_smaller_element(arr:list):
    i,j=0,0
    
    while(i<len(arr)):
        print("What is being considered",arr[i])
        if (arr[i]> arr[j]):
            arr[i]=arr[j]
            i+=1
            j=i
        else:
            j+=1
        if j>=len(arr)-1:
            arr[i]=-1
            i+=1
    return arr

print(next_smaller_element([4, 8, 5, 2, 25]))
print(next_smaller_element([13, 7, 6, 12]))