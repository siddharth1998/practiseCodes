import array

class Dynamic_array:
    def __init__(self,icap=1,typecode='l'):
        self._array=array.array(typecode,[0]*icap)
        self.icap=icap
        self.size=0
        self.typecode=typecode
        
    def __double_array(self):
        temp=self._array
        self._array=array.array(self.typecode,[0]*self.size*2)
        self.icap=self.icap*2
        for i in range(self.size):
            self._array[i]=temp[i]
    
    def __half_array(self):
        temp=self._array
        self._array=array.array(self.typecode,[0]*(self.icap//2))
        self.icap=self.icap//2
        for index,ele in enumerate(temp):
            if ele==0:
                break
            self._array[index]=ele
        
        
    def insert(self,element):
        if self.size==self.icap:
            self.__double_array()
        self._array[self.size]=element
        self.size+=1
    
    def delete(self,element):
        index=0
        while(index<=self.size):
            if element==self._array[index]:
                self.size-=1
                self._array[index]=self._array[self.size]
                self._array[self.size]=0
                
                
                if self.size <= (self.icap//2) and self.icap > 1:
                    self.__half_array()
                return True
            index+=1
            
        return False
x=Dynamic_array()
x.insert(1)
print("Size increasing of array gradually")
print(x._array)
print("size",x.size)
x.insert(2)
print(x._array)
print(x.icap)
x.insert(2)
x.insert(3)
x.insert(4)

print("Size decreasing of array gradually")
print(x._array)

x.delete(4)
print(x._array)
x.delete(3)
print(x._array)
x.delete(2)
print(x._array)
x.delete(1)
print(x._array)