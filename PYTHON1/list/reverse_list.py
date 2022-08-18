a=[1,2,3,4,5,6,7,8]
print(a)
a.reverse()
print(a)

b=[]
n=int(input("enter the length of the list:"))
for i in range(1,n+1):
    ele=input("enter the elements:")
    b.append(ele)
print("before reverse the list:",b)
ele=[]
for i in reversed(b):
    ele.append(i)
print("after reverse the list:",ele)
