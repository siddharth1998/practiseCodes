#program to check AP 
from tokenize import Token
from tracemalloc import start

sequence=input("Print the number of sequence in spaced format  ::")
print(sequence)
# sequence='1 3 5 7'
list=sequence.split(' ')
list2=[]
print(list)
token=False
def checkAP():
    global token
    counter=0
    lcounter=0
    for i in list:
        i=int(i)
        if counter >=1:
            last=i
            difference=last-start
            start=i
            list2.append(difference)
            if lcounter-1>=0: 
                if difference==list2[lcounter-1]:
                    token=True
                else:
                    Token=False
                    print("not AP")
                    break
            counter=counter+1
            lcounter=lcounter+1
            print(list2)
        else :
            counter=counter+1
            start=i

checkAP()
if token==True:
    print("This is AP")