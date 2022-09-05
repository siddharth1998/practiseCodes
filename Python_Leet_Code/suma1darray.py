class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        total=0
        tempDict=[]
        for i in nums:
            total=total+i
            tempDict.append(total)
        return(tempDict)