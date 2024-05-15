def ans(query:str,output:str):
    # print(query,",", output)
    if len(query)==0: # base case 
        print(output)
        return 
    ans(query[1:],output+query[0])
    ans(query[1:],output)#not pick

if __name__=="__main__":
    ans("abc","")
    print("----")