def user_reverse(a):
    c=0
    for i in range(len(a)):
        c=c+1
    print("count:",c)
    for i in range(c//2):
        temp=a[i]
        a[i]=a[c-i-1]
        a[c-i-1]=temp
    print("after the list :",a)

a=[]
n=int(input("enter the no.of elements:"))
for i in range(0,n):
    ele=int(input("enter the elements:"))
    a.append(ele)
print("before reverse the list is :",a)
user_reverse(a)
