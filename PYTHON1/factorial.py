def factorial(num):
    while(num > 0):
        if(num==1):
            return 1
        else:
            return num*factorial(num-1)


num=int(input("enter a number:"))
n=factorial(num)
print(n)
