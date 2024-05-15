def divider(main_list:list)->bool:
    total=0
    # Get the toal Sumation of the list 
    for i in main_list:
        total+=i
    

    def recur(choosen:list,sum)->bool:
        # print(choosen,sum,total)
        if choosen==[]:
            return # base case
        
        if total-sum==sum:
            print("Found")
            return True
        #pick OR    #not pick 
        
        return True if recur(choosen[1:],sum+choosen[0]) or recur(choosen[1:],sum) else False
    return recur(main_list,0)

if __name__=="__main__":
    print(divider([1,7,5,10,3]))
        