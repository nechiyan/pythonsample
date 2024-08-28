s = "aabbcc"

#The function f(s) analyzes the count of characters in a given string and 
# returns a dictionary with each unique character as a key and its count as the value.
#suppose s is the string
def f(s):
    r = {}  # Create an empty dictionary 'r' to store the character counts
    for i in s: # Loop through each character in the string 's'
        if i in r:  # Check if the character is already in the dictionary 'r'
            r[i] += 1  # Increment the count if found.
        else:
            r[i] = 1  # else Add the character to the dictionary with an initial count of 1 .
    return r # After processing all characters, return the dictionary 'r'


result = f(s)
print(result)

 #Use collections.Counter, which is optimized for counting hashable items
from collections import Counter

def f(s):
    return Counter(s)

result = f(s)
print(result)

