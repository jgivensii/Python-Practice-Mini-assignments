# -*- coding: utf-8 -*-
"""
Created on Thu Jan  1 19:04:04 2026

@author: jgive
"""
word = input("Enter your word: ")
print(f"This is your word: {word}")

size = len(word)
revWord = ""

print(f"Your word has this many letters: {size}")

"""
Use range when using a int to loop as it a creates a range
from 0 to the integer which is the size of the inputted word 
"""

for i in range(size):
    revWord += word[size - 1 - i]
    
print(f"Reversed word: {revWord}")

if word == revWord:
    print(f"{word} is a palindrome.")

else: 
    print(f"{word} is not a palindrome.")
    