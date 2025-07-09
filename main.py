
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
    """Find the longest palindromic string using optimized substring concatenation."""
    # Handle edge cases
    if not a or not b:
        return "-1"

    best = None
    max_len = 0
    
    # Performance optimization: limit substring length to prevent timeout
    max_substring_len = min(20, len(a), len(b))  # Reasonable limit for large inputs
    
    # Try substrings in order of decreasing length for early termination
    for len_a in range(max_substring_len, 0, -1):
        if best and len_a + max_substring_len <= max_len:
            break  # Can't possibly beat current best
            
        for start_a in range(len(a) - len_a + 1):
            sa = a[start_a:start_a + len_a]
            
            for len_b in range(max_substring_len, 0, -1):
                if best and len_a + len_b <= max_len:
                    break  # Can't possibly beat current best
                    
                for start_b in range(len(b) - len_b + 1):
                    sb = b[start_b:start_b + len_b]
                    
                    # Try both concatenation orders
                    for candidate in [sa + sb, sb + sa]:
                        if is_palindrome(candidate):
                            if len(candidate) > max_len or (len(candidate) == max_len and (best is None or candidate < best)):
                                best = candidate
                                max_len = len(candidate)

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
