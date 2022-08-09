num=int(input("enter the number"))
print(num)
temp=num
rev=0
while num > 0:
    rev=rev*10+num%10
    num=num//10
if(temp==rev):
    print(temp ,"is palindrome")
else:
    print(temp, "is not a palindrome")
