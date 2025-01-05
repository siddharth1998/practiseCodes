from heap import Heap


x = Heap()
x.elements = [10, 8, 5, 7, 6, 9]
x._Heap__bubble_up(len(x.elements) - 1)  # last index
print("Result :: ", x.elements)
x.insert(11)
x.print_heap()
res=x.top()
print("Result ",res)
x.print_heap()

res=x.top()

print("Result ",res)
x.print_heap()

res=x.top()

print("Result ",res)
x.print_heap()

x.heapify([1,2,10,4,5,6])
x.print_heap()