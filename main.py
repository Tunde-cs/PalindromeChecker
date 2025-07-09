
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
    
    # Create extended string pools that include reversed versions
    # This allows us to find palindromes like "abc" + "cba" = "abccba"
    extended_a = a + a[::-1]  # Original + reverse
    extended_b = b + b[::-1]  # Original + reverse
    
    # Try all possible substring combinations with longer substrings prioritized
    # Process in reverse order of length to find longer palindromes first
    for len_a in range(len(extended_a), 0, -1):
        for start_a in range(len(extended_a) - len_a + 1):
            sa = extended_a[start_a:start_a + len_a]
            
            for len_b in range(len(extended_b), 0, -1):
                for start_b in range(len(extended_b) - len_b + 1):
                    sb = extended_b[start_b:start_b + len_b]
                    
                    # Try both concatenation orders: sa+sb and sb+sa
                    for candidate in [sa + sb, sb + sa]:
                        if is_palindrome(candidate):
                            cand_len = len(candidate)
                            # Update if longer, or same length but lexicographically smaller
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
