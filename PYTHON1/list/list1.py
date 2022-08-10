
a=[1,2,3,4,5]
print(a)
b=[]
print(b)
c=[1.1,2.2,3.3,4.4]
print(c)
d=["aaa","bbbb","ccc","ddd"]
print(d)
e=[1,"aaa",1.1]
print(e)
f=[]
print(f)
g=[1,2,3,[4,5,6],7]
print(g)

a1=[]
n=int(input("enter the number of elements:"))
for i in range(0,n):
    ele=int(input())
    a1.append(ele)
print(a1)

a11=[]
n=int(input("enter the number of elements:"))
for i in range(0,n):
    ele=float(input())
    a11.append(ele)
print(a11)

a111=[]
n=int(input("enter the number of elements:"))
for i in range(0,n):
    ele=(input())
    a111.append(ele)
print(a111)
