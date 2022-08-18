a=[1,2,3,4,5,6,7,8]
print(a)
print(sum(a))

b=[]
n=int(input("enter the no.of elements in the list:"))
for i in range(0,n):
    ele=int(input("enter the elements in the list:"))
    b.append(ele)
print(b)
print("sum of the elements in the list is:",sum(b))

c=[]
n=int(input("enter the no.of elements in the list:"))
for i in range(0,n):
    element=int(input("enter the elements in the list:"))
    c.append(element)
print(c)
sum=0
for i in c:
    sum=sum+i
print("sum of the elements in the list is:",sum)
