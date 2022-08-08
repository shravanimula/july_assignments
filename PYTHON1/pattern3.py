'''
5
4 4
3 3 3
2 2 2 2
1 1 1 1 1
'''
rows=int(input("enter the no.of rows:"))
num=5
for i in range(rows,0,-1):
    for j in range(rows,i-1,-1):
        print(num ,end=" ")
    print("\n")
    num=num - 1
