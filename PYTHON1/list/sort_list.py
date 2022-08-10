a=[66,33,99,22,88,11,55]
print(a)
a.sort()
print(a)
'''
a1=[99,44,22,88,44,77]
print(a1)
for i in range(len(a1)):
    for j in range(i+1,len(a1)):
        if a[i] > a[j]:
            a1[i], a1[j]=a1[j], a1[i]
print(a1)
'''
list=[]
n=int(input("Please enter the no.of elements: "))
for i in range(1, n+1):
    value= int(input("Please enter the Value of element:"))
    list.append(value)
for i in range (n):
    for j in range(i + 1, n):
        if(list[i] > list[j]):
            temp = list[i]
            list[i] = list[j]
            list[j] = temp
print(list)
