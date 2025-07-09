
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

def can_form_palindrome(char_count):
    """Check if given character counts can form a palindrome."""
    odd_count = sum(1 for count in char_count.values() if count % 2 == 1)
    return odd_count <= 1

def build_palindrome_from_chars(char_count):
    """Build the lexicographically smallest palindrome from character counts."""
    if not can_form_palindrome(char_count):
        return None
    
    # Build first half of palindrome
    first_half = []
    middle = ""
    
    # Sort characters to ensure lexicographically smallest result
    for char in sorted(char_count.keys()):
        count = char_count[char]
        # Add half of each character's count to first half
        first_half.extend([char] * (count // 2))
        # If count is odd, save one for middle
        if count % 2 == 1:
            middle = char  # Only one odd count allowed for palindrome
    
    # Build palindrome: first_half + middle + reversed_first_half
    first_half_str = ''.join(first_half)
    palindrome = first_half_str + middle + first_half_str[::-1]
    
    return palindrome

def buildPalindrome(a, b):
    """Find the longest palindromic string by concatenating substrings or rearranging characters."""
    # Handle edge cases
    if not a or not b:
        return "-1"
    
    best_substring = None
    max_substring_len = 0
    
    # APPROACH 1: Try substring concatenation first
    for i in range(len(a)):
        for j in range(i + 1, len(a) + 1):
            sa = a[i:j]
            
            for k in range(len(b)):
                for l in range(k + 1, len(b) + 1):
                    sb = b[k:l]
                    
                    # Try both concatenation orders: sa+sb and sb+sa
                    for candidate in [sa + sb, sb + sa]:
                        if is_palindrome(candidate):
                            cand_len = len(candidate)
                            # Update if this is longer, or same length but lexicographically smaller
                            if (cand_len > max_substring_len or 
                                (cand_len == max_substring_len and (best_substring is None or candidate < best_substring))):
                                best_substring = candidate
                                max_substring_len = cand_len
    
    # APPROACH 2: Try character rearrangement
    all_chars = Counter(a + b)
    best_rearrange = build_palindrome_from_chars(all_chars)
    
    # Choose the best result
    candidates = []
    if best_substring:
        candidates.append((best_substring, max_substring_len))
    if best_rearrange:
        candidates.append((best_rearrange, len(best_rearrange)))
    
    if not candidates:
        return "-1"
    
    # Sort by length (descending), then lexicographically (ascending)
    candidates.sort(key=lambda x: (-x[1], x[0]))
    return candidates[0][0]

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
