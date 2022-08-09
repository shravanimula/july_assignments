def even(min,max):
    for i in range(min,max+1):
        if (i%2)==0:
            print(i, "is even")


min=int(input("enter the minimum number:"))
max=int(input("enter the maximum number:"))
even(min,max)

def odd(min,max):
    for i in range(min,max+1):
        while (i%2)!=0:
            print(i,"is odd")
            break
min=int(input("enter the minimum number:"))
max=int(input("enter the maximum number:"))
odd(min,max)
