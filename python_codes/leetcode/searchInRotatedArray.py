class Solution:
    def search(self, nums: list[int], target: int) -> int:
        mid_index=len(nums)//2

        end_index=len(nums)-1

        start_index=0
        while(start_index<end_index):
            print(start_index,mid_index,end_index)
            if nums[mid_index]==target or nums[end_index]==target or nums[start_index]==target:
                
                return mid_index
            else:
                if nums[mid_index]>target:
                    
                if nums[mid_index]>nums[end_index]:
                    #search in right side of the mid
                    start_index=mid_index+1
                    # pass
                else:
                    # search in the left side of the mid 
                    end_index=mid_index-1
                    # pass
            mid_index=(start_index+end_index)//2
        return -1
    
x=Solution()
print(x.search([4,5,6,7,0,1,2],6))