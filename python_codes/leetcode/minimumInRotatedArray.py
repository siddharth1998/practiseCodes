class Solution:
    def findMin(self, nums: list[int]) -> int:
        # find if mid > end
        # then rotated then search in second half 
        # else search in first half and do the binary search on the rest of the items
        #  send first element in list <-- 2

        mid_index=len(nums)//2
        end_index=len(nums)-1
        start_index=0
        # flag=1
        lowest=nums[mid_index]
        while(abs(start_index-end_index)>1):
            # print("start_index,mid_index,end_index")

            if nums[mid_index]>nums[end_index]:
                start_index=mid_index
                # flag=1
                
            else:
                end_index=mid_index
                # flag=0
            
            mid_index=(start_index+end_index)//2
            lowest=nums[mid_index] if nums[mid_index]< lowest else lowest
          
        # if nums[start_index]<nums[end_index]:
        lowest=nums[start_index] if lowest > nums[start_index] else lowest
        # else:
        lowest=nums[end_index] if lowest > nums[end_index] else lowest

        return lowest
    
x=Solution()
print(x.findMin([3,4,5,6,7,8,-1,1,2]))
print(x.findMin([0,1,2,3,4]))
print(x.findMin([2,1]))

