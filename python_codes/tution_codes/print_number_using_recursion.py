def printing_num(n:int):
    
    if(n<=0):
        print(n,end=" -- ")
        return
    else:
        printing_num(n-1)
        print(n,end=" -- ")

if __name__=="__main__":
    printing_num(10)