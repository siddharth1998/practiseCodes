class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        # write your code here
        temp=''
        for i in strs:
            temp=temp+i+'||0||'
        return(temp)
        

    
    """
    @param: str: A string
    @return: decodes a single string to a list of strings
    """
    def decode(self, str):
        return(str.split("||0||"))
        # write your code here
x=Solution()
y=x.encode(['a','b','c||0||','chicka'])
z=x.decode(y)
