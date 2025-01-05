import array
class circular_queue:
    def __init__(self,length=3):
        self.cqueue=array.array('d',[0]*length)
        self.rear=0
        self.front=0
        self.length=length
        
    def enqueue(self,value:int)->bool:
        '''
        Insert at the rear
        '''
        if self.cqueue[self.rear]==0:
            self.cqueue[self.rear]=value
            self.rear=(self.rear+1)%self.length
            return True 
        return False
    
    def dequeue(self)->int:
        if self.cqueue[self.front]!=0:
            result=self.cqueue[self.front]
            self.cqueue[self.front]=0
            self.front=(self.front+1)%self.length
            return result
        else:
            return None
    
    def __str__(self):
        counter=0
        indexer=self.front
        print("Start ->",end=" ")
        while(counter < self.length):
            print(self.cqueue[indexer],end=" --> ")
            indexer=(indexer+1)%self.length
            counter+=1
        print(" END ")
        return ""
obj=circular_queue(3)
print(obj.enqueue(8))
print(obj.enqueue(9))
print(obj.enqueue(10))
print ("After queue",obj)
print(obj.dequeue())
print ("After Dequeue",obj)

print(obj.enqueue(11))
print (obj)

print(obj.dequeue())
print(obj.dequeue())
print(obj.dequeue())
print(obj.dequeue())
print(obj)

