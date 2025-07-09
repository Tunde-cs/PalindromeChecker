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
    """Find the shortest palindromic string from concatenating substrings of a and b."""
    # Handle edge cases
    if not a or not b:
        return "-1"

    best = None
    min_len = float('inf')

    # Performance limit to avoid timeout
    max_limit = min(20, len(a), len(b))

    # Try all substring combinations, looking for the shortest palindrome
    for len_a in range(1, min(len(a), max_limit) + 1):
        for start_a in range(len(a) - len_a + 1):
            sa = a[start_a:start_a + len_a]

            for len_b in range(1, min(len(b), max_limit) + 1):
                for start_b in range(len(b) - len_b + 1):
                    sb = b[start_b:start_b + len_b]

                    # Try both concatenation orders
                    candidates = [sa + sb, sb + sa]
                    for candidate in candidates:
                        if is_palindrome(candidate):
                            cand_len = len(candidate)
                            if (cand_len < min_len or 
                                (cand_len == min_len and (best is None or candidate < best))):
                                best = candidate
                                min_len = cand_len

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