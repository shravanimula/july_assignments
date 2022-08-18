#swap the elements with temp
a=int(input("enter the a number:"))
b=int(input("enter the b number:"))
print("before swap the elements are:","a=",a,"b=",b)
temp=a
a=b
b=temp
print("after swap the elements are:","a=",a,"b=",b)

#swap the elements without temp

a=int(input("enter the a number:"))
b=int(input("enter the b number:"))
print("before swap the elements are:","a=",a,"b=",b)
a=a ^ b
b=a ^ b
a=a ^ b
print("after swap the elements are:","a=",a,"b=",b)

#swap the elements without temp


a=int(input("enter the a number:"))
b=int(input("enter the b number:"))
print("before swap the elements are:","a=",a,"b=",b)
a = a + b
b = a - b
a = a - b
print("after swap the elements are:","a=",a,"b=",b)


