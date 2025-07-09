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
    """Find the longest palindromic string using substring concatenation."""
    # Handle edge cases
    if not a or not b:
        return "-1"

    best = None
    max_len = 0

    # Try all possible substring combinations
    for i in range(len(a)):
        for j in range(i + 1, len(a) + 1):
            sa = a[i:j]

            for k in range(len(b)):
                for l in range(k + 1, len(b) + 1):
                    sb = b[k:l]

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