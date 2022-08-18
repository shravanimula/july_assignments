'''
count() returns the number of occurrences of substring sub in the range [start,end]
start and end are interpreted as in slice notation
'''
'''
str.count(sub,start=0,end=len(string))
sub − This is the substring to be searched.

start − Search starts from this index. First character starts from 0 index. By default search starts from 0 index.

end − Search ends from this index. First character starts from 0 index. By default search ends at the last index.
'''
str="hello india ,good morning"
sub="o"
print("the string is:",str)
print("the sub string is:",sub)
print(str.count(sub,4,20))

str1="thundersoft in india in hyd"
sub="in"
print("the string is:",str1)
print("the sub string is:",sub)
print(str1.count(sub))

string=input("enter the string:")
sub=input("enter the sub string:")
print("the string is:",string)
print("the sub string is:",sub)
print("count the sub in strings in the main string:",string.count(sub))
