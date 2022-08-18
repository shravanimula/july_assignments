'''
isdecimal()-It is a function in Python that returns true if all characters in a string are decimal. If all characters are not decimal then it returns false.
Syntax:
    string_name.isdecimal()
    Parameters:This method does not takes any parameters .
    Returns Value:
        True – all characters are decimal
        False – one or more then one character is not decimal
'''

string="123456"
print(string)
print(string.isdecimal())

string="12345 6789"
print(string)
print(string.isdecimal())

string="1234aaaa"
print(string)
print(string.isdecimal())


string="a1111"
print(string)
print(string.isdecimal())

string="1234 aaaa"
print(string)
print(string.isdecimal())


