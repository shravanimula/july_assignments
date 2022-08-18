'''
find:
Python String find() method returns the lowest index or first occurrence of the substring if it is found in a given string. If it is not found then it returns -1

Syntax:

    str.find(sub, start, end)
    Parameters: 

        sub: It is the substring that needs to be searched in the given string. 
        start: Starting position where the substring needs to be checked within the string. 
        end: End position is the index of the last value for the specified range. It is excluded while checking. 
'''
string="thundersoft india in hyd"
sub="in"
print("string:",string)
print("sub:",sub)
print(string.find(sub))
print(string.find(sub,5,11))
print(string.find(sub,14))
print(string.find(sub,1,25))
print(string.find(sub,13,20))

