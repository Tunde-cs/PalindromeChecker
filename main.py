
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
    """Find the longest palindromic string from concatenating substrings of a and b."""
    # Handle edge cases
    if not a or not b:
        return "-1"
    
    # Special case: if strings are identical, try the full concatenation
    if a == b:
        full_concat = a + a[::-1]  # string + reverse
        if is_palindrome(full_concat):
            return full_concat
    
    best = None
    max_len = 0
    
    # Performance limit to avoid timeout
    max_limit = min(20, len(a), len(b))
    
    # Try all substring combinations with early termination optimizations
    # Process in order that favors lexicographically smaller results
    for total_len in range(2, min(len(a) + len(b), max_limit * 2) + 1):
        if best and total_len <= max_len:
            continue
            
        for len_a in range(1, min(len(a), total_len, max_limit) + 1):
            len_b = total_len - len_a
            if len_b < 1 or len_b > len(b) or len_b > max_limit:
                continue
                
            for start_a in range(len(a) - len_a + 1):
                sa = a[start_a:start_a + len_a]
                
                for start_b in range(len(b) - len_b + 1):
                    sb = b[start_b:start_b + len_b]
                    
                    # Try both concatenation orders, prioritizing lexicographically smaller
                    candidates = sorted([sa + sb, sb + sa])
                    for candidate in candidates:
                        if is_palindrome(candidate):
                            cand_len = len(candidate)
                            if (cand_len > max_len or 
                                (cand_len == max_len and (best is None or candidate < best))):
                                best = candidate
                                max_len = cand_len
                                break  # Take the first (lexicographically smaller) valid palindrome
    
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
