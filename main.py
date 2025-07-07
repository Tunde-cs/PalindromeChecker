#!/bin/python3

import math
import os
import random
import re
import sys

def buildPalindrome(a, b):
    if not a or not b:
        return "-1"

    def is_palindrome(s):
        return s == s[::-1]

    best = None

    # Optimization: use only reasonable length substrings to avoid TLE
    max_len = min(len(a), len(b), 10)

    # Generate all substrings (not subsequences) of a and b
    def get_substrings(s):
        substrings = set()
        n = len(s)
        for i in range(n):
            for j in range(i + 1, n + 1):
                substrings.add(s[i:j])
        return substrings

    sa = get_substrings(a)
    sb = get_substrings(b)

    for x in sa:
        for y in sb:
            for combo in [x + y, y + x]:
                if is_palindrome(combo):
                    if (best is None or
                        len(combo) > len(best) or
                        (len(combo) == len(best) and combo < best)):
                        best = combo

    # Special edge case: if a == b, return a + reversed(a)
    if a == b:
        candidate = a + a[::-1]
        if is_palindrome(candidate):
            if (best is None or
                len(candidate) > len(best) or
                (len(candidate) == len(best) and candidate < best)):
                best = candidate

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