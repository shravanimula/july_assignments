'''
1
2 2
3 3 3 
4 4 4 4
5 5 5 5 5
'''
rows=int(input("enter the no.of rows:"))
num=1
for i in range(0,rows):
    for j in range(0,i+1):
        print(num ,end=" ")
    print("\n")
    num=num+1
