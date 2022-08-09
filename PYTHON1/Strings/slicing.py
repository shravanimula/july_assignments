str="thundersoft india hyd"
print(str)
print(str[:])
print(str[:10])
print(str[5:])
print(str[:-1])
print(str[1:10:2])
print(str[-1:-10:-2])
c=0
for i in str:
    print("s[%d]:"%c,i)
    c+=1
