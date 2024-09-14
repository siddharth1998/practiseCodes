
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
    
    def linearSearch(self,element):
        for i in range(len(self.rarray)):
            if element == self.rarray[i] :
                return element 
            if element < self.rarray[i] :
                # value at i is greater than element 
                return None 
    
    def binarySearch(self,target):
        left=0
        right=self._usage
        mid=None
        while(left <= right):
            mid=(right+left)//2
            if self.rarray[mid]==target:
                return mid
            elif self.rarray[mid]<target:
                left=mid+1
            else:
                right=mid-1

    def duplicate_binary_search(self,target):
        left=0 
        right=len(self.rarray)-1
        while(left < right):
            mid=(left+right)//2
            if self.rarray[mid]==target:
                return mid
            elif self.rarray[mid]<target:
                left=mid+1
                if mid<len(self.rarray)-1:
                    while(self.rarray[mid]==self.rarray[mid+1]):
                        mid+=1
                left=mid+1
            else:
                right=mid-1
                if mid>1:
                    while(self.rarray[mid]==self.rarray[mid-1]):
                        mid-=1
                right=mid-1

x=sarray_ops(5)
x.insert(1)
x.insert(2)
x.insert(4)
x.insert(5)
x.insert(3)
x.delete(3)
x.delete(1)
x.insert(1)
x.insert(3)
x.delete(1)
x.insert(3)


print("The linear search ", x.linearSearch(1))
print("The duplicate linear search ",x.duplicate_binary_search(3))
print("Normal Binary search ",x.binarySearch(3))
print(x.rarray)