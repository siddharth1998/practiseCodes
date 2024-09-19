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
        
    def insert(self,element):
        if self.size==self.icap:
            self.__double_array()
        self._array[self.size]=element
        self.size+=1
        
x=Dynamic_array()
x.insert(1)
print(x._array)
print("size",x.size)
x.insert(2)
print(x._array)
print(x.icap)
x.insert(2)
print(x._array)