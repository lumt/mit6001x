# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 16:39:19 2016

@author: apple
"""

s = 'jmlusqellpomeyxgvc'

longest = s[0]
temp = s[0]

for i in range(1, len(s)):
    if s[i] >= s[i-1]: # increasing order
        # append current
        temp += s[i]
        if len(temp) > len(longest):
            longest = temp
    else:
        # not in increasing order
        temp = s[i]
            
print("Longest substring in alphabetical order is: " + str(longest))

