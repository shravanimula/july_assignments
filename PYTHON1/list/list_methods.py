a=[1,2,3,4,5]
print(a)
print(id(a))
b=[11,22,33,44]
print(b)
print(id(b))
print(a + b)#concatenation
print(id(a))
print(4 in a)#check membership
print(6 in a)

#append 
a=[]
n=int(input("enter the number of elements:"))
print(n)
for i in range(0,n):
    ele=int(input())
    a.append(ele)
print(a)


a1=[1,2,3,4]
print(a1)
a1.append(5)
print(a1)
#a.append(6,7) #it will give Typeerror
#print(a)

def fun(a):
    c=0
    for i in a:
        c+=1
    print("count:",c)
    print(a)

a=[1,2,3,4,5,6]
fun(a)

def fun(a1):
    print(a1)
    b=[11,22,33]
    a1.extend(b)
    print(a1)
a1=["aaa","bbbb","ccc"]
fun(a1)
