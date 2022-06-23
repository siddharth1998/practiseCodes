#armstorg number 

number=int(input("Please input the Number :: "))
def isArm(number):
    sum=0
    strNumber=str(number)
    for i in strNumber: 
        sum=sum+int(i)**3

    if (sum==number):
        print(True)
        return(True)
    else:
        print(False)
        return(False)

answer=isArm(number)
if answer==True:
    print("The number is Armstrong number")
else: 
    print("This not Armstrong number")