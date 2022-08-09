#function without arguments and without return type
def fun():
    print('Hello,good morning')
fun()

#fucntion without arguments,with return type
def fun1():
    a=10
    b=20
    return a+b
result=fun1()
print(result)

#function with argument and without return value

def fun(n):
    n=n+10
    print(n)

num=int(input("enter the num"))
fun(num)

#function with argument and with return value
def fun(x,y):
    result=x+y
    return result
a=int(input("enter the number:"))
b=int(input("enter the number:"))
sum=fun(a,b)
print(sum)

