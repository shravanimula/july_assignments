a=int(input('enter a number:'))
b=int(input('enter b number:'))
if a > b:
    print('a is greater than b')
else:
    print('b is greater than a')


c=int(input('enter c value:'))
d=int(input('enter d value:'))
e=int(input('enter e value:'))
if c > d and c > e:
    print('c is greater than d and e')
elif d > c and d > e:
    print('d is greater than c and e')
elif e > c and e > d:
    print('e is greater than c and d')
else :
    print('all are equal')

