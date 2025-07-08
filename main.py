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

    # Try all contiguous substrings from both strings
    # Case 1: substring from a + substring from b
    for i in range(n):
        for j in range(i + 1, n + 1):
            sa = a[i:j]
            for k in range(m):
                for l in range(k + 1, m + 1):
                    sb = b[k:l]

                    # Try both orders: sa+sb and sb+sa
                    candidates = [sa + sb, sb + sa]

                    for candidate in candidates:
                        if candidate == candidate[::-1]:  # is palindrome
                            if len(candidate) > max_len or (len(candidate) == max_len and (best == "-1" or candidate < best)):
                                best = candidate
                                max_len = len(candidate)

    return best

if __name__ == '__main__':
    t = int(input())
    for case in range(t):
        a = input().strip()
        b = input().strip()
        result = buildPalindrome(a, b)
        print(result)