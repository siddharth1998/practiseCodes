

def threeSum(nums: list[int]) -> list[list[int]]:
    nums.sort() # sort it as the we have to send the numbers not the index 
    result=list()

    counter=0
    while(counter < len(nums)-1):
        if(nums[counter]==nums[counter-1] and counter > 0):
            counter+=1
            continue
        left=counter+1
        right=len(nums)-1
        
        
       
        while(left<right):

            sum= nums[left]+nums[right] + nums[counter]
            if sum==0:
                result.append([nums[counter],nums[left],nums[right]])
                left+=1
                while(nums[left]==nums[left-1] and left < right):
                    left+=1
                
                right-=1
            elif sum > 0 :
                right-=1
            elif sum < 0 : 
                left +=1
            
        counter+=1
    return result

            # target=nums[fix]*-1
            # left=fix+1# left will be one ahead from fixated point
            
            # right=len(nums)-1# right will always start from end 
            # print("fix", nums[fix])
            
            # while(left<right):
            #     sum=nums[left]+nums[right]
            #     if sum == target:
            #         result.append([nums[fix],nums[left],nums[right]])
            #         print("At , ",nums[fix]," Left",nums[left], "right", nums[right])
            #         print("elemenet previous to left element", nums[left-1])
            #         while (nums[left]==nums[left-1] and left < right   ):
            #             left+=1
            #             print("Left changed to ",nums[left])
            #         print("Outside left",nums[left])
            #         left+=1
            #         ref=left
            #         right-=1
            #     elif sum > target : 
            #         ref=fix+1
            #         right-=1
            #     elif sum < target : 
            #         ref=fix+1
            #         left +=1
            # fix=ref
            # counter+=1
       
    return result
    
print(threeSum([-1,0,1,2,-1,-4]))
print(threeSum([0,0,0,0,1,-1]))
print(threeSum([0,0,0,0]))
print(threeSum([-2, 0, 0, 2, 2]))





      # distinct set
#         # [i,j,k] => i + j + k =0 
#         # target = 0 
        
#         left=0
        
#         result_set=set()
#         # 1. Get unique elements
#         need_set= set(nums)
#         need_list=list(nums)# unique elements list
#         need_list.sort() # O nlog(n)
#         right=1
#         min=need_list[0]
#         max=need_list[-1]
#         print("The list is ",need_list)
#         hash_map={}
#         while(left<right and right< len(need_list)):

#             need= (need_list[left]+need_list[right])*-1

#             if need < min or need > max:
#                 pass
#             else:
#                 if (left,right) in hash_map:
#                      pass
#                 else:
#                     hash_map[(left,right)]=need

   
#             left+=1
#             right+=1

#         print(hash_map)
#         temp_list=need_list.copy()
#         for i in hash_map:
#             try:
#                 temp_list.remove(need_list[i[0]])
#                 temp_list.remove(need_list[i[1]])
#             except:
#                  pass
#             if hash_map[i] in temp_list:
#                  result_set.add((need_list[i[0]],need_list[i[1]],hash_map[i]))
            
            
#         result_set=list(result_set)
#         result_list=[list(x) for x in result_set]
      
        
          
#         return(result_list)


# def threeSumApp1(nums: list[int]) -> list[list[int]]:
#         # distinct set
#         # [i,j,k] => i + j + k =0 
#         # target = 0 
        
#         left=0
        
#         result_list=[]
#         # 1. Get unique elements
#         need_set= set(nums)
#         need_list=list(nums)# unique elements list
#         need_list.sort() # O nlog(n)
#         right=len(need_list)-1
#         print("The list is ",need_list)
#         while(left<right):
            
#             need= (need_list[left]+need_list[right])*-1
#             if need in need_set:
#                 temp_list=need_list.copy()
#                 temp_list.remove(need_list[left])
#                 temp_list.remove(need_list[right])
#                 if need in temp_list:
#                      result_list.append([need_list[left],need_list[right],need])


#             elif need > 0 : 
#                 right-= 1
#                 continue
#             elif need < 0 :
#                 left+= 1
#                 continue 
#             else: 
#                 right-=1
#             left+=1
#             right-=1
#         return(result_list)