'''
expandTabs()
 Returns a string by replacing all the ‘\t’ characters with white space characters.

string.expandtabs(tabsize)

Tabsize(optional): integer value that determines the number of white space characters before the next character. If not provided, the default value is 8.
'''
str="hello\tgood morning\t"
print(str)
print(str.expandtabs())
print(str.expandtabs(10))

str1="hello thundersoft\tindia\thyd123"
print(str1)
print(str1.expandtabs())
print(str1.expandtabs(10))
