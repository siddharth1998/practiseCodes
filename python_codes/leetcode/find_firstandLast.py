class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        length=len(nums)
        offset=0
        if length==0:
            return [-1,-1]
        loc1,loc2=-1,-1
        # divide the list in two 
        # check the list range 
        # move according to that range if both become [] return [-1,-1]
        l1,l2=nums[0:length//2],nums[length//2+1:]
        def recurCall(l1,l2,offset):
            if(l1[-1]==target):
                return 
            pass
        # while(l1 or l2):
        #     if l1[-1]>=target and l2[0]!=target:
        #         nums=l1#the number is in l1 range
        #     else if l1[-1]==target and l2[0]==target:
        #         # add code to handle the two list continuation
        #         pass
        #     else:
        #         offset=len(l1)-1+offset
        #         if l2[0]==target:
        #             loc1=len(l1)
        #         nums=l2
        #         #the number is in l2 range
        #     l1,l2=nums[0:length//2],nums[length//2+1:]
            
        return [loc1,loc2]