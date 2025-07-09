
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
    
    best = None
    max_len = 0
    
    # Try all possible substring combinations
    # For each substring from a
    for i in range(len(a)):
        for j in range(i + 1, len(a) + 1):
            sa = a[i:j]
            
            # For each substring from b
            for k in range(len(b)):
                for l in range(k + 1, len(b) + 1):
                    sb = b[k:l]
                    
                    # Try both concatenation orders: sa+sb and sb+sa
                    for candidate in [sa + sb, sb + sa]:
                        if is_palindrome(candidate):
                            cand_len = len(candidate)
                            # Update if this is longer, or same length but lexicographically smaller
                            if (cand_len > max_len or 
                                (cand_len == max_len and (best is None or candidate < best))):
                                best = candidate
                                max_len = cand_len
    
    return best if best else "-1"

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
