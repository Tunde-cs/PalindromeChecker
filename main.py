
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
    """Find the longest palindromic string by concatenating substrings from a and b."""
    # Handle edge cases
    if not a or not b:
        return "-1"
    
    # Try all possible combinations and collect all palindromes
    palindromes = []
    
    # Try all possible substring combinations from the original strings only
    for len_a in range(1, len(a) + 1):
        for start_a in range(len(a) - len_a + 1):
            sa = a[start_a:start_a + len_a]
            
            for len_b in range(1, len(b) + 1):
                for start_b in range(len(b) - len_b + 1):
                    sb = b[start_b:start_b + len_b]
                    
                    # Try both concatenation orders: sa+sb and sb+sa
                    for candidate in [sa + sb, sb + sa]:
                        if is_palindrome(candidate):
                            palindromes.append(candidate)
    
    if not palindromes:
        return "-1"
    
    # Sort by length (descending) then lexicographically (ascending)
    palindromes.sort(key=lambda x: (-len(x), x))
    return palindromes[0]

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
