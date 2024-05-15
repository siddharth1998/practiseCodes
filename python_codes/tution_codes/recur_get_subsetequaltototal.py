def finder(val,target,total):
    # print(val,total)
    
    if total==target:
        print(val, total)
        return True
    if val==[]:
        return False
    
    #pick 
    return finder(val[1:],target,total+val[0]) or finder(val[1:],target,total)

if __name__=="__main__":
    print("Starting")
    print(finder([1,2,3],10,0))