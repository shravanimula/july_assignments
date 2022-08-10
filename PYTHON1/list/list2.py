a=[1,2,3]
print(a)
print(id(a))
a[2]=30
print(a)
print(id(a))

a=a+["aaaa","bbbb"]
print(a)
print(id(a))

a1=[1,2,11,55]
n=len(a1)
print(n)
print(a1)
print(id(a1))
for i in range(n):
    print(a1[i])

a2=[1,"aaa",11.55,22,"ccccc",22.2]
print(a2)
for i in range(len(a2)):
    print(a2[i])
