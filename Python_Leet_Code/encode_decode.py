def encode(strs: list[str]) -> str:
        encoded=''
        for i in strs: 
            encoded+=str(f'{len(i):3}')+i
        return(encoded)
def decode(strs:str)-> list:
        result=[]
        while(strs) :
                length=int(strs[0:3])
                word=strs[3:length+3]
                result.append(word)
                strs=strs[length+3:]
        print(result)            
x=encode(["hi","there"])
print(x)
y=decode(x)