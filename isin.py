"""
Created on Fri Sep 16 00:27:38 2016

@author: apple
"""

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    if len(aStr) < 1:
        return False
    if len(aStr) == 1:
        return char == aStr

    mid = len(aStr)// 2
    
    if char == aStr[mid]:
        return True
    elif char < aStr[mid]:
        return isIn(char, aStr[:mid])
    elif char > aStr[mid]:
        return isIn(char, aStr[mid:])
