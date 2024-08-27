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

# import unittest
# from collections import Counter

# def f(s):
#     return Counter(s)

# class TestCharacterFrequency(unittest.TestCase):
#     def test_empty_string(self):
#         self.assertEqual(f(''), Counter())
    
#     def test_single_character(self):
#         self.assertEqual(f('a'), Counter({'a': 1}))
    
#     def test_multiple_characters(self):
#         self.assertEqual(f('aabbcc'), Counter({'a': 2, 'b': 2, 'c': 2}))
    
#     def test_special_characters(self):
#         self.assertEqual(f('abc!@#'), Counter({'a': 1, 'b': 1, 'c': 1, '!': 1, '@': 1, '#': 1}))

# if __name__ == '__main__':
#     unittest.main()
