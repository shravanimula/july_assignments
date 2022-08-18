a=[11,22,33,44,88,66,55]
print(a)
print(max(a))

b=[]
n=int(input("enter the number of elements in the list:"))
for i in range(0,n):
    ele=int(input("enter the elements in the list:"))
    b.append(ele)
print(b)
print(max(b))


c=[]
n=int(input("enter the number of elements in the list:"))
for i in range(0,n):
    ele=int(input("enter the elements in the list:"))
    c.append(ele)
print(c)
max=0
for i in c:
    if i > max:
        max=i
print("maximum number in the list:",max)

