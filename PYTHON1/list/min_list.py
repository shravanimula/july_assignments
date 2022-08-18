a=[111,22,33,44,88,66,55,11]
print(a)
print(min(a))

b=[]
n=int(input("enter the number of elements in the list:"))
for i in range(0,n):
    ele=int(input("enter the elements in the list:"))
    b.append(ele)
print(b)
print("minimum number in the list:",min(b))


c=[]
n=int(input("enter the number of elements in the list:"))
for i in range(0,n):
    ele=int(input("enter the elements in the list:"))
    c.append(ele)
print(c)
min=c[0]
for i in c:
    if i < min:
        min=i
print("minimum number in the list:",min)

