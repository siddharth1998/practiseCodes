class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #brute force method
        #hash map 
        tdict={}
        for i in t:
            if i in tdict:
                tempDict={i:tdict[i]+1}
                tdict.update(tempDict)
            else:
                tdict[i]=1
        
        for i in s:
            if i in tdict and tdict[i]>0 and len(s)==len(t):
                tempDict={i:tdict[i]-1}
                tdict.update(tempDict)
            else:
                return(False)
        return(True)
                