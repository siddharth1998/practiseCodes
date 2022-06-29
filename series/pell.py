from numpy import number


def pellCreator(position):
    start=0
    second=1
    i=0
    if position==1:
        print('0')
    
    if position==2:
        print('0 1')
    else:
        print('0 1 ',end="") 
        while (i+2 <= position):
            pellnumber= start + second*2
            print(pellnumber,end=" ")
            i=i+1
            start=second
            second=pellnumber

if __name__=="__main__":
    position=input("Please input the poistion till which you want print the pell number :: ")
    pellCreator(int(position))