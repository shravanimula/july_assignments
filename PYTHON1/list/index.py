b=[1,2,3,4,5]
print(b)
print(b.index(4))

def fun_index(a):
    print("the elements are:")
    print(a)
    ele=int(input("enter the element to  print the index:"))
    print(a.index(ele))
    
list=[]
n=int(input("enter the no.of elements:"))
print("enter the list elements:")
for i in range(0,n):
    ele=int(input())
    list.append(ele)
fun_index(list)

#print the index using elements
def fun_index1(a):
    print("the list string elements are:")
    print(a)
    ele=(input("enter the string to  print the index:"))
    print(a.index(ele))
    
list=[]
n=int(input("enter the no.of elements:"))
print("enter the list of strings are:")
for i in range(0,n):
    ele=input()
    list.append(ele)
fun_index1(list)

