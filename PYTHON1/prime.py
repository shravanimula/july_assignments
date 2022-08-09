
def prime():
    a=int(input("enter a number:"))
    for i in range(2,a):
        if a%i == 0:
            flag = False
            break;
        else:
            flag=True
    if flag:
        print("given number is prime number:",a)
    else:
        print("given number is not prime number:",a)
prime()


min=int(input("enter the minimum number:"))
max=int(input("enter the maximum number:"))
for i in range(min,max+1):
    for j in range(2,i):
        if (i%j)==0:
            break
    else:
        print(i)

def prime_range(min,max):
    for i in range(min,max+1):
        for j in range(2,i):
            if (i%j)==0:
                break
        else:
            print(i)
min=int(input("enter the minimum number:"))
max=int(input("enter the maximum number:"))
prime_range(min,max)

