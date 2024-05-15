class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # sort the list
        nums.sort()
        lindex=0
        rindex=len(nums)-1
        result_list=[]

        while(lindex<rindex):
            print(nums)
            found=False
            movement=0
            what_is_required=0-(nums[lindex]+nums[rindex])

            if(what_is_required>=0):
                zindex=lindex+1
                movement=1
            elif(what_is_required<0):
                zindex=rindex-1
                movement=-1
            else:
                #0,0,0
                found=True
                
                result_list.append((nums[lindex],0,nums[rindex],))
            
            while(zindex!=lindex and zindex!=rindex):
                if nums[zindex]==what_is_required:
                    found=True
                    if [nums[lindex],nums[zindex],nums[rindex]] in result_list:
                        pass
                    else:
                        result_list.append([nums[lindex],nums[zindex],nums[rindex]])
                zindex+=movement
                print(nums[zindex],nums[rindex],nums[lindex],what_is_required)
            print("exit")
            if found:
                print("found")
                lindex+=1
                rindex-=1
            else:
                if movement>0:
                    lindex+=1
                elif movement<0:
                    rindex-=1
                print(lindex,rindex)
        
        return result_list


x=Solution()
print(x.threeSum([-2,0,1,1,2]))
