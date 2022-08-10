#insert the elements
def fun(a,n):
    for i in range(0,n):
        print(a[i])
    a.insert(3,99)
    print(a)
    a.insert(10,100)
    print(a)
    return a


list=[]
n=int(input("enter the no.of elements:"))
for i in range(0,n):
    ele=(input())
    list.append(ele)
fun(list,n)
print(list)


