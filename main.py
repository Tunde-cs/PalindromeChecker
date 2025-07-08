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

    if not a or not b:
        return "-1"

    # Right-to-left approach: try to build palindromes by matching characters from ends
    # For each possible left part from a, try to find matching right part from b
    for left_len in range(1, n + 1):
        left_part = a[:left_len]
        target_right = left_part[::-1]  # What we need on the right to make palindrome
        
        # Try to find this target in b (from right side)
        for right_start in range(m - len(target_right) + 1):
            if b[right_start:right_start + len(target_right)] == target_right:
                # Found matching right part, now add remaining characters in middle
                middle = a[left_len:] + b[:right_start] + b[right_start + len(target_right):]
                palindrome = left_part + middle + target_right
                
                if len(palindrome) > max_len or (len(palindrome) == max_len and (best == "-1" or palindrome < best)):
                    best = palindrome
                    max_len = len(palindrome)

    # Try the reverse: left part from b, right part from a
    for left_len in range(1, m + 1):
        left_part = b[:left_len]
        target_right = left_part[::-1]
        
        for right_start in range(n - len(target_right) + 1):
            if a[right_start:right_start + len(target_right)] == target_right:
                middle = b[left_len:] + a[:right_start] + a[right_start + len(target_right):]
                palindrome = left_part + middle + target_right
                
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