class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #brute force method
        #hash map 
#         tdict={}
#         for i in t:
#             if i in tdict:
#                 tempDict={i:tdict[i]+1}
#                 tdict.update(tempDict)
#             else:
#                 tdict[i]=1
        
#         for i in s:
#             if i in tdict and tdict[i]>0 and len(s)==len(t):
#                 tempDict={i:tdict[i]-1}
#                 tdict.update(tempDict)
#             else:
#                 return(False)
#         return(True)
        tmap={}
        smap={}
        if len(s)==len(t):
                for i in range(len(s)):
                    tmap[t[i]]=tmap.get(t[i],0)+1 #putting the value of the letter if it is preset it will add or put 0 
                    smap[s[i]]=smap.get(s[i],0)+1
                if tmap==smap:
                    return(True)
                else:
                    return(False)
        else:
            return(False)