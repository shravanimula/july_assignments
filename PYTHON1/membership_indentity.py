#in membership operator

a=10
b=7
list=[1,2,3,4,5,6,7,8,9]
if(a in list):
    print("a is present in the list:")
else:
    print("a is not present in the list:")
if(b in list):
    print("b is present in the list:")
else:
    print("b is not present in the list:")

#Not in membership operator
a=23
b=33
list1=[11,22,33,44,55,66]
if(a not in list1):
    print("a is not present in the list:")
else:
    print("a is present in the list:")
if(b not in list1):
    print("b is not present in the list:")
else:
    print("b is present in the list:")


#in membership operator
a="aaa"
b="bb"
tuple=("aaa","bbb","ccc","ddd")
if(a in tuple):
    print("a is present in the tuple:")
else:
    print("a is not present in the tuple:")
if(b in tuple):
    print("b is present in the tuple:")
else:
    print("b is not present in the tuple:")

#Not in membership operator
a=22
b=32
tuple1=(11,22,33,44,55,66)
if(a not in tuple1):
    print("a is not present in the tuple1:")
else:
    print("a is present in the tuple1:")
if(b not in tuple1):
    print("b is not present in the tuple1:")
else:
    print("b is present in the tuple:")

#is identity operator

a1=(1,2,3,4,5,6,7,8,9)
b1=(1,2,3,4,5,6,7,8,9)
if(a1 is b1):
    print("a1 and b1 are same tuple")
else:
    print("a and b are not same in the not tuple")

#isnot identity operator
a=(1,2,3,4,5,6,7,7)
b=(1,2,3,4,5,6,7,7)
if(a is not b):
    print("a and b are not same in the tuple")
else:
    print("a and b are same the tuple")
