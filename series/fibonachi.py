# this is a code for using fibonachi 
position1=int(input(" Please enter the possition "))
#0,1,1,2,3,5
counter=0
list1=[]
def fib(postion1):
    counter=0
    if (position1==1):
        print(0)
    elif (postion1==2):
        print("0,1")
    else:
        counter=counter+3
        start=0
        after=1
        list1.append(0)
        list1.append(1)
        while(counter<=postion1): 
        #print(counter)i
            varFib=start+after
            start=after
            after=varFib
            counter=counter+1
            list1.append(varFib)
        print(list1)
fib(position1) 
