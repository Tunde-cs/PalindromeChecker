#!/bin/python3

import math
import os
import random
import re
import sys
import time

def is_palindrome(s):
    return s == s[::-1]

def buildPalindrome(a, b):
    best = None
    max_len = 0
    max_limit = 20  # Performance limit

    # Early exit for empty strings
    if not a or not b:
        return "-1"

    for len_a in range(1, min(len(a), max_limit) + 1):
        # Early termination if we can't possibly beat current best
        if best and len_a + len(b) <= max_len:
            continue

        for start_a in range(len(a) - len_a + 1):
            sa = a[start_a:start_a + len_a]

            for len_b in range(1, min(len(b), max_limit) + 1):
                # Early termination
                if best and len_a + len_b <= max_len:
                    continue

                for start_b in range(len(b) - len_b + 1):
                    sb = b[start_b:start_b + len_b]

                    for cand in [sa + sb, sb + sa]:
                        if is_palindrome(cand):
                            if len(cand) > max_len or (len(cand) == max_len and (best is None or cand < best)):
                                best = cand
                                max_len = len(cand)

    return best if best else "-1"

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