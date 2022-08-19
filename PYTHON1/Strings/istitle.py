'''
Python String istitle() Method is a built-in string function that returns True if all the words in the string are title cased, otherwise returns False.

syntax:  string.istitle()
title:
When all words in a string begin with uppercase letters and the remaining characters are lowercase letters, the string is called title-cased.  This function ignores digits and special characters.
'''
string="Thundersoft India Hyd"
print(string)
print(string.istitle())

string="THUNDERSOFT INDIA"
print(string)
print(string.istitle())

string="thundersoft india hyd"
print(string)
print(string.istitle())

string="thundersoftindia"
print(string)
print(string.istitle())


string="ThundersoftIndiaHyd"
print(string)
print(string.istitle())


string="Thundersoft India Hyd123"
print(string)
print(string.istitle())

string="Thundersoft123India11Hyd"
print(string)
print(string.istitle())

string="Thundersoft123IndiaHyd11"
print(string)
print(string.istitle())

