a=[1,2,3,4,5]
print(a)
a.clear()
print(a)


#clear  the int element from the list
def fun_clear(a,n):
    print("print the int elements are:")
    for i in range(0,n):
        print(a[i])
    print(a)
    a.clear()
    return a


list=[]
n=int(input("enter the no.of elements:"))
print("enter the list elements:")
for i in range(0,n):
    ele=int(input())
    list.append(ele)
fun_clear(list,n)
print(list)

#clear  the element from the list
def fun_clear(a,n):
    print("print the elements are:")
    for i in range(0,n):
        print(a[i])
    print(a)
    a.clear()
    return a


list=[]
n=int(input("enter the no.of elements:"))
print("enter the elements:")
for i in range(0,n):
    ele=input()
    list.append(ele)
fun_clear(list,n)
print(list)

