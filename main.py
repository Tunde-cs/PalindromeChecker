#!/bin/python3

import math
import os
import random
import re
import sys

def is_palindrome(s):
    return s == s[::-1]

def buildPalindrome(a, b):
    # Early exit for empty strings
    if not a or not b:
        return "-1"

    best_palindrome = None
    max_length = 0

    n = len(a)
    m = len(b)

    # Try all possible substrings from both strings
    for i in range(n):
        for j in range(i + 1, n + 1):
            sa = a[i:j]
            for k in range(m):
                for l in range(k + 1, m + 1):
                    sb = b[k:l]

                    # Try both sa + sb and sb + sa
                    for combo in [sa + sb, sb + sa]:
                        if is_palindrome(combo):
                            # Check if this is better than current best
                            if (len(combo) > max_length or 
                                (len(combo) == max_length and 
                                 (best_palindrome is None or combo < best_palindrome))):
                                best_palindrome = combo
                                max_length = len(combo)

    return best_palindrome if best_palindrome else "-1"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for _ in range(t):
        a = input().strip()
        b = input().strip()

        result = buildPalindrome(a, b)

        fptr.write(result + '\n')

    fptr.close()