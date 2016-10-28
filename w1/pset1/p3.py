"""
Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters occur in alphabetical order. For example, if s = 'azcbobobegghakl', then your program should print

Longest substring in alphabetical order is: beggh
In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print

Longest substring in alphabetical order is: abc
"""

longest = s[0]
temp = s[0]

for i in range(1, len(s)):
    # if current is larger than previous append
    if s[i] >= s[i-1]: 
        temp += s[i]
        if len(temp) > len(longest):
            longest = temp
    # not in increasing order
    else:
        temp = s[i]
            
print("Longest substring in alphabetical order is: " + str(longest))