from collections import defaultdict 

class Solution:
    def isAnagramFromSol(self,s,t):
        count=defaultdict(int)
        for i in s:
            count[i]+=1
        for j in t:
            count[j]-=1
        for i in count:
            if count[i]!=0:
                return False
        return True



    def isAnagram(self, s: str, t: str) -> bool:
        temp_dict={}
        for i in s : 
            # is already there operation
            if i in temp_dict:
                temp_dict[i]+=1
            else:
                temp_dict[i]=1
        
        # Anagram checker for second string
        for i in t:
            # if i not in temp_dict :=> return False
            # if i in temp_dict :=> temp_dict[i]-1
            # if i in temp_dict[i] =<0 return False


            if i not in temp_dict: 
                return False
            else : 
                if temp_dict[i]==0:
                    return False
                temp_dict[i]-=1
            if temp_dict[i]<=0:
                temp_dict.pop(i)
        if temp_dict=={}:
            return True
        else:
            return False
a=Solution()
print(a.isAnagramFromSol("anagram","nagaraqm"))