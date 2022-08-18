'''
index:
The index() method returns the index of a substring inside the string (if found). If the substring is not found, it raises an exception.
Syntax: 
    ch.index(ch1, begp, endp)
    Parameters: 
    ch1 : The string to be searched for.
    begp (default : 0) : This function specifies the position from where search has to be started. 
    endp (default : string_len) : This function specifies the position from where search has to end.
    Return Value: 
    Returns the first position of the substring found.
    Exception: 
    Raises ValueError if argument string is not found.
    '''
str="thundersoft india in hyd"
sub="in"
print(str)
print(sub)
print(str.index(sub))
print(str.index(sub,2,14))
print(str.index(sub,14))
string=input("enter the string:")
sub=input("enter the sub string:")
print("string is:",string)
print("sub string is:",sub)
print(string.index(sub))
print(string.index(sub,11,20))
