'''
Objective:
Write a function that takes two words as an argument and returns true if they are
anagrams (contain the exact same letters) and false otherwise.
'''

def isAnagram(string1, string2):
    string1, string2 = str(string1), str(string2)
    string1charcounts, string2charcounts = {}, {}
    isanagram = True
    if (len(string2) != len(string2)): #checks if they are different lengths (most obvious indicator)
        isanagram = False
    for char in string1: #counts the characters in the first string
        if (char not in string1charcounts):
            string1charcounts[char] = 1
        else:
            string1charcounts[char] += 1
    for char in string2: #counts the characters in the second string
        if (char not in string2charcounts):
            string2charcounts[char] = 1
        else:
            string2charcounts[char] += 1
    for charcounts in string1charcounts: #compares the character counts
        if (charcounts not in string2charcounts):
            isanagram = False
        elif (string2charcounts[charcounts] != string1charcounts[charcounts]):
            isanagram = False
    return isanagram