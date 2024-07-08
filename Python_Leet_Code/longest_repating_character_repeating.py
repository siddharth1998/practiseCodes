def func(s:str,k:int):
    # populate the mapper function 
    count_of_alphabets_list=[0]*26#[0, 0, ..., 0]
    max_longest=0
    l=0

    for r in range(len(s)):
        # Increase the count of alphabets
        count_of_alphabets_list[ord(s[r])-65]+=1
        # compare the validity of the window you are parsing
        while((r-l+1)-max(count_of_alphabets_list)>k):
            # Decrease the count of the l as substring won't be longer than that
            count_of_alphabets_list[ord(s[l])-65]-=1
            l+=1
        
        max_longest=max(max_longest,(r-l)+1)


    return max_longest


# print(func(['A','B','A','B','B','Z','A'],k=2))
print(func("AABABBA",k=1))