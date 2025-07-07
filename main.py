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

    # Collect all possible palindromes
    palindromes = []

    n = len(a)
    m = len(b)

    for i in range(n):
        for j in range(i + 1, n + 1):
            sa = a[i:j]
            for k in range(m):
                for l in range(k + 1, m + 1):
                    sb = b[k:l]

                    # Try both sa + sb and sb + sa (without reversing)
                    for combo in [sa + sb, sb + sa]:
                        if is_palindrome(combo):
                            palindromes.append(combo)

    if not palindromes:
        return "-1"

    # Find the maximum length
    max_length = max(len(p) for p in palindromes)

    # Filter palindromes with maximum length
    max_palindromes = [p for p in palindromes if len(p) == max_length]

    # Return the lexicographically smallest among maximum length palindromes
    return min(max_palindromes)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for _ in range(t):
        a = input().strip()
        b = input().strip()

        result = buildPalindrome(a, b)

        fptr.write(result + '\n')

    fptr.close()