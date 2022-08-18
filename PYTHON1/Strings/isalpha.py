'''
The isalpha() methods returns “True” if all characters in the string are alphabets, Otherwise, It returns “False”.  
Syntax: 
    string.isalpha()
Parameters:
      isalpha() does not take any parameters
   Returns:
   True: If all characters in the string are alphabet.
   False: If the string contains 1 or more non-alphabets.
   Errors and Exceptions:
1.It contains no arguments, therefore an error occurs if a parameter is passed
2.Both uppercase and lowercase alphabets return “True”
3.Space is not considered to be the alphabet, therefore it returns “False”
'''
string="thundersoft"
print(string)
print(string.isalpha())

string="THUNDERSOFT"
print(string)
print(string.isalpha())

string="THUNDERsoft"
print(string)
print(string.isalpha())

string="123thundersoft"
print(string)
print(string.isalpha())

string="thunder soft"
print(string)
print(string.isalpha())

string="thunder soft 123"
print(string)
print(string.isalpha())

string=input("enter the string:")
print(string)
print(string.isalpha())


