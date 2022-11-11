'''Name of the problem 
Duplicate Zeros

link to the problem
https://leetcode.com/explore/learn/card/fun-with-arrays/525/inserting-items-into-an-array/3245/

problem statement
Given a fixed-length integer array arr, duplicate each occurrence of zero, shifting the remaining elements to the right.

Note that elements beyond the length of the original array are not written. Do the above modifications to the input array in place and do not return anything.

 

Example 1:

Input: arr = [1,0,2,3,0,4,5,0]
Output: [1,0,0,2,3,0,0,4]
Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]

Example 2:

Input: arr = [1,2,3]
Output: [1,2,3]
Explanation: After calling your function, the input array is modified to: [1,2,3]

 

Constraints:

    1 <= arr.length <= 104
    0 <= arr[i] <= 9



'''
#your solution
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        #started doing with map but the index was getting updated
        
        orglength=len(arr)#original length
        length=len(arr)#dynamic Length
        index=0
        
        print(length)
        while (index<length):
            # print("index {} -->{} ==> {}".format(index,arr[index],tempCount))
            if arr[index]==0:
                arr.insert(index,0)
                index=index+1
                length=len(arr)
           
          
                if index==length:
                    print("come")
                    arr.append(0)
                if index > length:
                    break
            index=index+1
   
        #code remove extra digits
        differ=length-orglength
        while (differ>0):
            differ=differ-1
            arr.pop()
        print(arr)
        
#         indexMap=[]
        
#         print(arr)
        
#         for index,val in enumerate(arr):
            
#             if val==0:
#                 indexMap.append(index)
#         arr=arr[0:length-1]
          
#         for i in indexMap:
#             arr.insert(i,0)
#         arr=arr[0:length-1]
#         print(arr)
        

#better solution 
