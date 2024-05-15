def factorial(n):
    if n==1:
        return 1
    else:
        return n*fibonacci(n-1)
    
if __name__=='__main__':
    print(fibonacci(int(input("Please enter a number \n"))))