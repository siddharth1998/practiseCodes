def isPalindrome( s: str) -> bool:
        headpos=0
        lastpos=len(s)-1
        while(headpos<=lastpos):
            if not s[headpos].isalnum():#https://www.w3schools.com/python/ref_string_isalnum.asp
                headpos+=1
                continue
            if not s[lastpos].isalnum():
                 lastpos-=1
                 continue
            
            if s[headpos].lower()==s[lastpos].lower():
                headpos+=1
                lastpos-=1
            else:
                return False
        return True 


print(isPalindrome("Was it a car or a cat I saw?"))