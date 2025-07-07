
#!/bin/python3

import math
import os
import random
import re
import sys

# Debug flag - set to False to disable debug output
DEBUG = True

def debug_print(msg):
    if DEBUG:
        print(msg)

def is_palindrome(s):
    return s == s[::-1]

def buildPalindrome(a, b):
    debug_print(f"DEBUG: Input a='{a}', b='{b}'")
    
    # Early exit for empty strings
    if not a or not b:
        debug_print("DEBUG: Empty string detected, returning -1")
        return "-1"
    
    # Generate all possible substrings from both strings
    substrings_a = []
    substrings_b = []
    
    # Extract all substrings from a
    for i in range(len(a)):
        for j in range(i + 1, len(a) + 1):
            substrings_a.append(a[i:j])
    
    # Extract all substrings from b
    for i in range(len(b)):
        for j in range(i + 1, len(b) + 1):
            substrings_b.append(b[i:j])
    
    debug_print(f"DEBUG: Substrings from a: {substrings_a}")
    debug_print(f"DEBUG: Substrings from b: {substrings_b}")
    
    best_palindrome = None
    max_length = 0
    
    # Try all combinations of substrings
    for sa in substrings_a:
        for sb in substrings_b:
            # Try both orderings: sa+sb and sb+sa
            candidates = [sa + sb, sb + sa]
            
            for candidate in candidates:
                debug_print(f"DEBUG: Testing candidate: '{candidate}' (from sa='{sa}', sb='{sb}')")
                
                if is_palindrome(candidate):
                    debug_print(f"DEBUG: Found palindrome: '{candidate}' (length {len(candidate)})")
                    
                    # Update best if this is longer, or same length but lexicographically smaller
                    if (len(candidate) > max_length or 
                        (len(candidate) == max_length and 
                         (best_palindrome is None or candidate < best_palindrome))):
                        
                        old_best = best_palindrome
                        best_palindrome = candidate
                        max_length = len(candidate)
                        debug_print(f"DEBUG: New best: '{best_palindrome}' (length {max_length}) - replaced '{old_best}'")
                    else:
                        debug_print(f"DEBUG: Palindrome '{candidate}' not better than current best '{best_palindrome}'")
                else:
                    debug_print(f"DEBUG: '{candidate}' is not a palindrome")
    
    debug_print(f"DEBUG: Final result: '{best_palindrome if best_palindrome else '-1'}'")
    return best_palindrome if best_palindrome else "-1"


if __name__ == '__main__':
    # Handle both submission environment and local testing
    if 'OUTPUT_PATH' in os.environ:
        fptr = open(os.environ['OUTPUT_PATH'], 'w')
    else:
        fptr = None

    t = int(input().strip())

    for _ in range(t):
        a = input().strip()
        b = input().strip()

        result = buildPalindrome(a, b)

        if fptr:
            fptr.write(result + '\n')
        else:
            print(result)

    if fptr:
        fptr.close()
