'''
string methods
1.capitalize()
'''
'''
returns a copy of the original string,with only the first letter as upper case and keeping all the other characters as lower case'''

a="THUNDERSOFT INDIA"
print(a)
print(a.capitalize())

b="Thunder Soft India"
print(b)
print(b.capitalize())

c="thunder soft india"
print(c)
print(c.capitalize())

d="thunDER sofT999 inDia"
print(d)
print(d.capitalize())

'''
2.casefold()
returns a string with each character as lower case '''
a="hello india"
print(a)
print("string casefold:",a.casefold())

b="Hello India"
print(b)
print("string casefold:",b.casefold())

c="HELLO INDIA"
print(c)
print("string casefold:",c.casefold())

d="heLLO,GooD 1morNINg "
print(d)
print("string casefold:",d.casefold())
