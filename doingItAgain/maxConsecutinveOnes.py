'''Name of the problem
Max Consecutive Ones

link to the problem
https://leetcode.com/explore/learn/card/fun-with-arrays/521/introduction/3238/

problem statement
Given a binary array nums, return the maximum number of consecutive 1's in the array.

 

Example 1:

Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.

Example 2:

Input: nums = [1,0,1,1,0,1]
Output: 2

 

Constraints:

    1 <= nums.length <= 105
    nums[i] is either 0 or 1.

'''

#your solution 

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        tempCount=0# real time changeing variable
        static=0# history variable 
      
        for i in nums:
            if i == 1:
                tempCount=tempCount+1
            else:   
                tempCount=0
            if static < tempCount:
                static=tempCount
        return static   
            
   
#better solution 
