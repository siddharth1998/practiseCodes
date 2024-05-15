number_of_steps=0
def tower(diskNo,start,end,middle):
        global number_of_steps
        if diskNo==1:
                print(f"Disk number {diskNo} from {start} to {end} ")
                number_of_steps+=1
        else:
                tower(diskNo-1,start,middle,end)
                print(f"Disk number {diskNo} from {start} to {end} ")
                number_of_steps+=1
                tower(diskNo-1,middle,end,start)
tower(4,"A","C","B")
print("Total number of steps",number_of_steps)