a=[11,22,33,44,55,66]
for i in a:
    print(i)

b=["aaa","bbb","cccc","dddd"]
for j in b:
    print(j)
    if j=="cccc":
        continue
    print(j)

a=('aaaa','bbbb','cccc','vvv','dddd')
for i in a:
    print(i)
    if i=='vvv':
        break

a=[1,2,3,4,5,6,7]
for i in a:
    print(i)
    if i==4:
        pass
