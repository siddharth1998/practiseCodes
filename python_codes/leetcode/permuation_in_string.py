class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        # s1 = ab 
        # s2 = bab ==> True

        # s1 = ab
        # s2 = acdb ==> False

        # s1 = ab
        # s2 = cdba ==> True

        # s1 = aa
        # s2 = cbaa ==> True

        # s1 = aa
        # s2 = acba ==> False

        # s1 = aba
        # s2 = eidbaa

        # s1= dac
        # s2 = dcddac

        # s1 = dac
        # s2 = cad

        # s1= abc 
        # s2= dedcadedcab

        count=0
        hashmap=dict()

        for i in s1:
            if i in hashmap:
                hashmap[i]+=1
            else:
                hashmap[i]=1
        temp_dict=hashmap.copy()

        while (count < len(s2)):
            if s2[count] in temp_dict:
                temp_count=0
                flag=True
                if len(s2)-count < len(s1):
                        return False
                while(temp_count < len(s1) and flag==True):
                    if s2[temp_count+count] in temp_dict and temp_dict[s2[temp_count+count]]>=1:
                        temp_dict[s2[temp_count+count]]-=1
                        flag=True
                    else:
                        # print(False)
                        flag=False
                    temp_count+=1  
                if flag==True:
                    return True
                else:
                    pass 
            temp_dict=hashmap.copy()
            

            count+=1
        return False
x=Solution()
print(x.checkInclusion("hello","ooolleoooleh"))