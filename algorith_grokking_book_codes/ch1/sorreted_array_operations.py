
# Insertion sort

from sorted_array import SortedArray
from array import array

class sarray_ops():
    def __init__(self,size,typeCode='l'):
        self._usage=0
        self.rarray=array(typeCode,[0]*size)
        self._size=size
    
    def insert(self,element):
        if self._usage==0:
            self.rarray[0]=element
            self._usage+=1
            return
        else:
            if self._usage >=self._size:
                raise ValueError("The array is already full")
            for i in range(self._usage,0,-1):
                if self.rarray[i-1] <=element:
                    self.rarray[i]=element
                    self._usage+=1
                    return
                else:
                    self.rarray[i]=self.rarray[i-1]
            self.rarray[0]=element
            self._usage+=1
        
    def delete(self,element):
        index=None
        for i in range(0,len(self.rarray)):
            if element==self.rarray[i]:
                index=i
                break

        if index==None:
            raise ValueError("The element given is not there in the array")
        
        for i in range(index,len(self.rarray)-1):
            self.rarray[i]=self.rarray[i+1]
        self.rarray[len(self.rarray)-1]=0
        self._usage-=1
   

x=sarray_ops(5)
x.insert(1)
x.insert(2)
x.insert(4)
x.insert(5)
x.insert(3)
print(x.rarray)
x.delete(3)
x.delete(1)
x.insert(1)
print(x.rarray)
