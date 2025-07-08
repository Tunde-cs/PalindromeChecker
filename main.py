#!/bin/python3

import math
import os
import random
import re
import sys

def buildPalindrome(a, b):
    best = "-1"
    max_len = 0
    n, m = len(a), len(b)

    # Early exit for empty strings
    if not a or not b:
        return "-1"

    # Try building palindromes using prefix from one string and suffix from another
    # The middle part comes from remaining characters
    
    # Case 1: Use prefix from a, suffix from b
    for prefix_len in range(1, n + 1):
        prefix = a[:prefix_len]
        remaining_a = a[prefix_len:]
        
        # Try to find matching suffix in b
        target_suffix = prefix[::-1]  # reverse of prefix
        
        # Check if we can form this suffix from b
        if len(target_suffix) <= m:
            # Try all possible ways to select suffix characters from b
            for start in range(m - len(target_suffix) + 1):
                if b[start:start + len(target_suffix)] == target_suffix:
                    middle = b[:start] + b[start + len(target_suffix):] + remaining_a
                    palindrome = prefix + middle + target_suffix
                    
                    if len(palindrome) > max_len or (len(palindrome) == max_len and (best == "-1" or palindrome < best)):
                        best = palindrome
                        max_len = len(palindrome)
    
    # Case 2: Use prefix from b, suffix from a  
    for prefix_len in range(1, m + 1):
        prefix = b[:prefix_len]
        remaining_b = b[prefix_len:]
        
        target_suffix = prefix[::-1]
        
        if len(target_suffix) <= n:
            for start in range(n - len(target_suffix) + 1):
                if a[start:start + len(target_suffix)] == target_suffix:
                    middle = a[:start] + a[start + len(target_suffix):] + remaining_b
                    palindrome = prefix + middle + target_suffix
                    
                    if len(palindrome) > max_len or (len(palindrome) == max_len and (best == "-1" or palindrome < best)):
                        best = palindrome
                        max_len = len(palindrome)

    return best

if __name__ == '__main__':
    t = int(input())
    for case in range(t):
        a = input().strip()
        b = input().strip()
        result = buildPalindrome(a, b)
        print(result)