'''
Python String isalnum() method checks whether all the characters in a given string are alphanumeric or not. Alphanumeric means a character that is either a letter or a number.
Syntax: 
    string_name.isalnum() 
    isalnum() method takes no parameters 
    Return: 
    True: If all the characters are alphanumeric 
    False: If one or more characters are not alphanumeric 
'''
a="thundersoftindia"
print(a)
print(a.isalnum())
b="thundersoft india"
print(b)
print(b.isalnum())
c="thundersoft123"
print(c)
print(c.isalnum())
d="123thundersoft"
print(d)
print(d.isalnum())
e=input("enter the string:")
print(e)
print(e.isalnum())
