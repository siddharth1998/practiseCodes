class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashMap=set()
        for i in nums:
            if i in hashMap:
                return(True)
            hashMap.add(i)
        return(False)
#brute force        
#         counter=0
#         for i in nums:
#             counter=0
#             for z in nums:
#                 if i==z:
#                     counter=counter+1  
#                 if counter>=2:
#                     break
#             if counter >= 2:
#                 return(True)
    
#         return(False)