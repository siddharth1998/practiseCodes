number=input("Print the number of sequence in spaced format  ::")

list=number.split(" ")
token=False
counter=0
problem=0
def checkGP():
    global list, counter,token, problem
    # if counter>0:
        
    #     pass
    # else:
    #     start=list[0    ]
    #     pass
    list2=[]
    lcounter=0
    for i in list:
        i=int(i)
        if counter>0 : 
            last=i
            
            modulo=last%start
            start=i
            list2.append(modulo)
            if lcounter-1>0:
                if modulo==list2[lcounter-1]:
                    token=True 
                else: 
                    token=False
                    problem=last
                    break
            lcounter=lcounter+1 
            counter=counter+1
        else: 
            counter=counter+1
            start=i
             
checkGP()
if token==True:
    print("This is a GP")
else:
    print("This is the wrong one :: {}".format(problem))
    print("This is not a GP")