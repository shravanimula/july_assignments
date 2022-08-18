'''
Python String isdigit() method returns “True” if all characters in the string are digits, Otherwise, It returns “False”. 
Python String isdigit() Method Syntax
Syntax: string.isdigit()

Parameters: isdigit() does not take any parameters

Returns:

    True – If all characters in the string are digits.
    False – If the string contains 1 or more non-digits.
'''

string="1234"
print(string)
print(string.isdigit())

string="123 4"
print(string)
print(string.isdigit())


string="1234aa"
print(string)
print(string.isdigit())


string=input("enter the string:")
print(string)
print(string.isdigit())

