class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # sorting the list 
        nums.sort()

        res=[]

        #efl element from left
        print(nums)
        for index, efl in enumerate(nums):
        
            if index > 0 and nums[index-1]==efl:# if present is equal to past 
                continue
            lindex,rindex=index+1,len(nums)-1
            while (lindex<rindex):

                required=efl+nums[lindex]+nums[rindex]
                print(index,lindex,rindex,required)
                
                if required < 0 :
                    lindex+=1
                elif required> 0:
                    rindex-=1
                else:
                    res.append([efl,nums[lindex],nums[rindex]])
                    lindex+=1
                    while(nums[lindex]==nums[lindex-1] and lindex < rindex):
                        lindex+=1
                # a+b+c=0
                #b+c=-a
        return res
     
x=Solution()
print(x.threeSum([-1,0,1,2,-1,-4]))