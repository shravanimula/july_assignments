a=int(input("enter a number:"))
b=int(input("enter b number:"))
if(a > b):
    print("a is greaterthan b")
else:
    print("b is greaterthan a")

a=int(input("enter the number:"))
if(a%2==0):
    print("a is even number")
else:
    print("a is odd number")

a=int(input("enter a number:"))
b=int(input("enter b number:"))
c=int(input("enter c number:"))
if( a > b and a > c):
    print("a is greater than b and c")
elif(b > a and b > c):
    print("b is greater than a and c")
elif(c > a and c > b):
    print("c is greater than a and b")
else:
    print("a,b and c are same")
