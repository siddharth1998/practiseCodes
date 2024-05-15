# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         hash_map=set()
#         for i in nums:
#             if i in hash_map:
#                 return True
#             else:
#                 hash_map.add(i)
#         return False
# Previos solution

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        # Using pointer method 
        nums.sort()
        i=0
        j=1
        if len(nums)==1:
            return False
        while(j<len(nums)):
            print(i," ",j)
            if nums[i]== nums[j]:
                return True
            i=i+1
            j=j+1
        return False
    def usingHashing(self,nums)-> bool:
        hash_map=set()
        for i in nums:
            if i in hash_map:
                return True
            else:
                hash_map.add(i)
        return False
 
a=Solution()
print(a.usingHashing([1,2,3,1]))