class Solution:
    def isPalindrome(self, s: str) -> bool:
        starting=0
        ending=len(s)-1
        both_correct=False
        while (starting<ending):
            temp_starting=s[starting]
            temp_ending=s[ending]
            both_correct=True
            if(s[starting].isalnum()):
                pass
            else:
                starting+=1
                temp_starting=s[starting]
                both_correct=False
            if(s[ending].isalnum()):
                pass
            else:
                ending-=1
                temp_starting=s[ending]
                both_correct=False
            if both_correct:
                
                if(temp_starting.lower()==temp_ending.lower()):
                    starting+=1
                    ending-=1
                else:
                    return False
        return True
    
x=Solution()
print(x.isPalindrome("i am don"))