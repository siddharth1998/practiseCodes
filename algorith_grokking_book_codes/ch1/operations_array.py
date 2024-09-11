from array import array

class CustomArray:
    def __init__(self,size,typeCode='l'):
        self._usage=0
        self.rarray=array(typeCode,[0]*size)
        self._size=size

    def inserting_into_array(self,element):
        if self._size <= self._usage:
            # raise Exception(IndexError,"Index out of range")
            raise IndexError("Index out of range")
        else:
            self.rarray[self._usage]=element
            self._usage+=1

    def delete(self,index):
        '''
        Swap the values from index and right most
        Then delete the last value
        '''
        if index > self._size:
            return "Index Out of bound"
        
        temp=self.rarray[-1]
        self.rarray[-1]=self.rarray[index]
        self.rarray[index]=temp
        temp=self.rarray[-1]
        self.rarray[-1]=0
        self._usage-=1
        return temp
    
    def find(self,value):
        '''
        As unsorted array will need to go through each element
        '''
        for i in range(0,self._usage):
            if self.rarray[i]==value:
                return self.rarray[i]
        return None
    

    def traverse(self,callback):
        '''
        Implementing something like map
        '''
        for i in range(self._usage):
            callback(self.rarray[i])




x=CustomArray(3)
print("Original",x.rarray)
x.inserting_into_array(1)
x.inserting_into_array(2)
x.inserting_into_array(2)
print("After Insertion",x.rarray)
print("Return value after deletion",x.delete(1))
print("After deletion",x.rarray)
x.traverse("Output of mapping like function",print)