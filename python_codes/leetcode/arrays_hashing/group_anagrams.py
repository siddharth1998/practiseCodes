from collections import defaultdict
class Solution():
    def groupAnagrams(self,strs:list[str]) -> list[list[str]]:
        # O(mxlog(n)x26)
        # m is the length of the list 
        # n is the length of the each element
        # 26 because the you will need to sort 26 such element
        result=defaultdict(list)
        for i in strs:
            x=list(i)
            x.sort()
            result["".join(x)].append(i)
        return result.values()
    def betterSolutionGroupAnagrams(self,strs:list[str]) -> list[list[str]]:
        # thank you neetcode for solution 
        result = defaultdict(list)

        for word in strs:
            count = [0]*26
            for letter in word:
                count[ord(letter)-ord('a')]+=1
            result[str(count)].append(word)
        return result.values()
    

objects=Solution()
output=objects.betterSolutionGroupAnagrams(["eat","tea","tan","ate","nat","bat"])
print(output)