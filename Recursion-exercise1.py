__author__ = 'Molly'

"""
Write a function that takes a string as a parameter and returns a new string that is the reverse of the old string.
"""

def reverseStr(str):
    if len(str) == 1:
        return str
    else:
        return str[-1] + reverseStr(str[:-1])

#print reverseStr("Molly")

"""
Write a function that takes a string as a parameter and returns True if the string is a palindrome, False otherwise.
"""



def palindromeChecker(str):
    print str
    if (len(str) == 2) and (str[0] == str[1]):
        return True
    if len(str) == 1:
        return True
    else:
        return (str[0] == str[-1]) and palindromeChecker(str[1:-1])

def removeSpace(str):
    newStr = ''
    for i in range(len(str)):
        if str[i] >= "a" and str[i] <= "z":
            newStr += (str[i])
    return newStr

print palindromeChecker(removeSpace("aibohphobia".lower()))
print palindromeChecker(removeSpace("Go hang a salami; I'm a lasagna hog.".lower()))