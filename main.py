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

    # Try all possible ways to combine characters from both strings
    # Method 1: Use prefix/suffix approach with all remaining chars in middle
    for i in range(n + 1):
        for j in range(m + 1):
            if i == 0 and j == 0:
                continue
                
            # Try taking first i chars from a and first j chars from b
            left = a[:i] + b[:j]
            remaining = a[i:] + b[j:]
            
            # Try to make palindrome: left + remaining + reverse(left)
            right = left[::-1]
            candidate = left + remaining + right
            
            if candidate == candidate[::-1]:
                if len(candidate) > max_len or (len(candidate) == max_len and (best == "-1" or candidate < best)):
                    best = candidate
                    max_len = len(candidate)
    
    # Method 2: Try simple substring concatenations  
    for i in range(n):
        for j in range(i + 1, n + 1):
            sa = a[i:j]
            for k in range(m):
                for l in range(k + 1, m + 1):
                    sb = b[k:l]
                    
                    for candidate in [sa + sb, sb + sa]:
                        if candidate == candidate[::-1]:
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