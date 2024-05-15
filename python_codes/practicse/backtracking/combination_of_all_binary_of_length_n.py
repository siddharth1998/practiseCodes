

def binary(n:int,arr:list):
	if n<1 :
		print(arr)
	else:
		arr[n-1]=0
		binary(n-1,arr)
		arr[n-1]=1
		binary(n-1,arr)

binary(5,[None]*5)
