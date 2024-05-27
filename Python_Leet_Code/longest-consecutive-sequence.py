def longestConsecutive(nums: list[int]) -> int:
        # hash_map={ value: count }
        set_map=list(set(nums))
        set_map.sort()
        print(set_map)
        max_val=1
        if nums==[]:
            return 0
        temp_holder=0
        for index,i in enumerate(set_map):
            temp_holder=max(max_val,temp_holder)
            if i+1 in set_map :
                max_val+=1
            elif index == len(set_map)-1 :
                continue 
            else:
                 max_val=1


        return temp_holder 
print(longestConsecutive([2,20,4,10,3,4,5]))