def productExceptSelf(nums: list[int]) -> list[int]:
        result=[]
        # [1,2,4,6]
        # LR = [1,1,2,8]
        # RL = [48,24,6,1]
        lp=[]
        rp=[]
        # L to R
        counter=0
        while(counter < len(nums)):
            if counter==0:
                product=1
            else:
                product=product*nums[counter-1]
            lp.append(product)
            counter+=1
        counter=len(nums)-1
        while(counter >= 0):
            if counter == len(nums)-1:
                product=1
            else:
                product=product*nums[counter+1]
            rp.insert(0,product)
            counter-=1
        
        # Populating the result 
        for index,i in enumerate(lp):
             product=lp[index]*rp[index]
             result.append(product)
        return result
x=productExceptSelf([-1,0,1,2,3])
print(x)