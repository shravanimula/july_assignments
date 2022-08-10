def fun_pop(a,n):
    for i in range(0,n):
        print(a[i])
    print(a)
    ind=int(input("enter the index to pop:"))
    a.pop(ind)
    print(a)


list=[]
size=int(input("enter the size of list:"))
print(size)
for i in range(0,size):
    ele=int(input())
    list.append(ele)
fun_pop(list,size)
