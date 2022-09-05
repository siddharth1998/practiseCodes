#  lsum=0
#         rsum=0
#         trigger=0
#         for z in range(1,len(nums)):
#                 rsum=rsum+nums[z]
#         for index, i in enumerate(nums):
#             if index==0:
#                 if rsum==0:
#                     print("rsum")
#                     return(0)
#                 if nums[0]<0:
#                     lsum=rsum-nums[1]-nums[-1]
#                 else:
#                     lsum=rsum+nums[0]-nums[-1]
#                 if lsum==0:
#                     print(rsum)
#                     print(nums[0])
#                     print(nums[-1])
#                     print("lsum")
#                     return(0)
#                 lsum=0
#             else:
               
#                 lsum=lsum+nums[index-1]
#                 rsum=rsum-i
#                 # print("left {}".format(lsum))
#                 # print("right {}".format(rsum))
#                 if lsum==rsum:
#                     return index
#         return -1
            
#                 # print("left {}".format(lsum))
#                 # print("right {}".format(rsum))
            
#             # if lsum-i==rsum-i:
#             #     return(index)
#             # else:
#             #     continue
        
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        #logic :: find the toal --> right total = total - the index number - sum of left
        total=sum(nums)
        leftSum=0
        for i in range(len(nums)):
            rightSum=total-nums[i]-leftSum
            if rightSum==leftSum:
                return(i)
            leftSum+=nums[i]
        return -1

#refered this : https://www.youtube.com/watch?v=u89i60lYx8U my approach was correct but was complex