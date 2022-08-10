#remove  the element from the list
def fun_remove(a,n):
    print("the elements are:")
    for i in range(0,n):
        print(a[i])
    print(a)
    element=int(input("enter the element to remove:"))
    a.remove(element)
    return a

list=[]
n=int(input("enter the no.of elements:"))
print("enter the elements:")
for i in range(0,n):
    ele=int(input())
    list.append(ele)
fun_remove(list,n)
print(list)



#remove  the string from the list
def fun_remove(a,n):
    print("the string elements are:")
    for i in range(0,n):
        print(a[i])
    print(a)
    element=(input("enter the string to remove:"))
    a.remove(element)
    return a


list=[]
n=int(input("enter the no.of elements:"))
print("enter the string elements:")
for i in range(0,n):
    ele=input()
    list.append(ele)
fun_remove(list,n)
print(list)

#remove  the float from the list
def fun_remove(a,n):
    print("the float elements are:")
    for i in range(0,n):
        print(a[i])
    print(a)
    element=float(input("enter the element to remove:"))
    a.remove(element)
    return a


list=[]
n=int(input("enter the no.of elements:"))
print("enter the float numbers:")
for i in range(0,n):
    ele=float(input())
    list.append(ele)
fun_remove(list,n)
print(list)


