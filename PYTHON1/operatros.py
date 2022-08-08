#addition and subtraction
a=5+3+2-4
print(a)

#multiplication and addition
a=10+5*2
print(a)

b=(10+5)*2
print(b)

#power of exponent
c=10**3
print(c)
c=c**2
print(c)

#logical operators
a=10
b=20
if(a and b ):
    print("a and b is :" ,True)
else:
    print("a and b is :" ,False)

a=1
b=0
if(a and b):
    print("a and b is:",True)
else:
    print("a and b is:",False)


a=10
b=0
if(a or b ):
    print("a and b is :" ,True)
else:
    print("a and b is :" ,False)

a=0
b=0
if(a or b):
    print("a and b is:",True)
else:
    print("a and b is:",False)

a=0
print("not of a is:",not a)

#bitwise operation

a=3
b=5
print("a and b is :",a & b)
print("a or b is:",a | b)
print(" a xor with b is:",a ^ b)
print("compliemt of a is :",~a)


#swap the variables
a=10
b=20
print("before swap a and b is :",a ,b)
a=a^b
b=a^b
a=a^b
print("after swap a and b is:",a ,b)


a=int(input("enter a number:"))
b=int(input("enter b number:"))
print("before swap a and b is:",a ,b)
a=a + b
b=a - b
a=a - b
print("after swap the variables are :",a ,b)
