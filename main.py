#!/bin/python3
import math
import os
import random
import re
import sys

def is_palindrome(s):
    return s == s[::-1]

def buildPalindrome(a, b):
    best = None
    max_len = 0

    # Early exit for empty strings
    if not a or not b:
        return "-1"

    # Check all possible substring combinations
    for len_a in range(1, len(a) + 1):
        for start_a in range(len(a) - len_a + 1):
            sa = a[start_a:start_a + len_a]

            for len_b in range(1, len(b) + 1):
                for start_b in range(len(b) - len_b + 1):
                    sb = b[start_b:start_b + len_b]

                    # Try both combinations: sa+sb and sb+sa
                    for cand in [sa + sb, sb + sa]:
                        if is_palindrome(cand):
                            # Update best if this is longer, or same length but lexicographically smaller
                            if len(cand) > max_len or (len(cand) == max_len and (best is None or cand < best)):
                                max_len = len(cand)
                                best = cand

    return best if best else "-1"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input().strip())
    for _ in range(t):
        a = input().strip()
        b = input().strip()
        result = buildPalindrome(a, b)
        fptr.write(result + '\n')
    fptr.close()