#!/bin/python3

import math
import os
import random
import re
import sys

def is_palindrome(s):
    """Check if a string is a palindrome."""
    return s == s[::-1]

def buildPalindrome(a, b):
    """Find the longest palindromic string from concatenating full strings a and b."""
    # Handle edge cases
    if not a or not b:
        return "-1"

    # Try both concatenation orders of the full strings
    candidates = [a + b, b + a]

    valid_palindromes = []
    for candidate in candidates:
        if is_palindrome(candidate):
            valid_palindromes.append(candidate)

    if not valid_palindromes:
        return "-1"

    # Return the longest palindrome, or lexicographically smallest if tied
    best = max(valid_palindromes, key=lambda x: (len(x), x))
    return best

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
```