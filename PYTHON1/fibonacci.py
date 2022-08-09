def fib(n):
    if(n==0):
        return 0
    elif (n==1):
        return 1
    else:
        return (fib(n-1) + fib(n-2))

num=int(input("enter a number:"))
result=fib(num)
print(result)

#print the series of fibannoci

def fib_series(n):
    a=0
    b=1
    c=0
    print(c)
    for i in range(1,n+1):
        a=b
        b=c
        c=a+b
        print(c)

num=int(input("enter the number:"))
fib_series(num)
