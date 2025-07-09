
#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

def is_palindrome(s):
    """Check if a string is a palindrome."""
    return s == s[::-1]

def buildPalindrome(a, b):
    """Find the longest palindromic string by rearranging all characters from a and b."""
    # Handle edge cases
    if not a or not b:
        return "-1"
    
    # Count all available characters
    char_count = Counter(a + b)
    
    # Check if we can form a palindrome
    odd_count = sum(1 for count in char_count.values() if count % 2 == 1)
    
    # For a palindrome, at most one character can have an odd count
    if odd_count > 1:
        return "-1"
    
    # Build the longest palindrome
    left_half = []
    middle = ""
    
    # Sort characters to ensure lexicographically smallest result
    for char in sorted(char_count.keys()):
        count = char_count[char]
        # Add half of the characters to the left side
        left_half.extend([char] * (count // 2))
        # If count is odd, this character goes in the middle
        if count % 2 == 1:
            middle = char
    
    # Create the palindrome: left_half + middle + reversed(left_half)
    left_str = ''.join(left_half)
    right_str = left_str[::-1]
    palindrome = left_str + middle + right_str
    
    return palindrome

if __name__ == '__main__':
    if 'OUTPUT_PATH' in os.environ:
        # Submission environment
        fptr = open(os.environ['OUTPUT_PATH'], 'w')
        t = int(input().strip())

        for _ in range(t):
            a = input().strip()
            b = input().strip()
            result = buildPalindrome(a, b)
            fptr.write(result + '\n')

        fptr.close()
    else:
        # Local testing
        t = int(input().strip())

        for _ in range(t):
            a = input().strip()
            b = input().strip()
            result = buildPalindrome(a, b)
            print(result)
