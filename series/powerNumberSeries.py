from turtle import position


def powerSeries(position,power):
    i=1
    while (i<=position):
        if i < position:
            print(i**power,end=", ")
        else :
            print(i**power)
        i=i+1

if __name__=="__main__":
    power=input("Please input the power you want :: ")
    position=input("Please input the postion :: ")
    powerSeries(int(position),int(power))