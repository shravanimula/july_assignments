'''
Python string method endswith() returns True if the string ends with the specified suffix, otherwise return False optionally restricting the matching with the given indices start and end.

Syntax
str.endswith(suffix, start, end)
Parameters
suffix − This could be a string or could also be a tuple of suffixes to look for.

start − The slice begins from here.

end − The slice ends here.
'''

str="hello ,good morning india"
suffix="i"
print(str)
print(str.endswith(suffix))
print(str.endswith(suffix,1,17))
print(str.endswith(suffix,1,21))

str1=input("enter the string:")
suffix=input("enter the specified string:")
print(str1)
print(suffix)
print(str.endswith(suffix))
