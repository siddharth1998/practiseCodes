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
        
   

x=sarray_ops(5)
x.insert(1)
x.insert(2)
x.insert(4)
x.insert(5)
x.insert(3)
print(x.rarray)
