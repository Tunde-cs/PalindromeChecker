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

    # Early exit for empty strings
    if not a or not b:
        return "-1"

    # Try all possible substrings with shorter ones first for lexicographic preference
    for total_len in range(2, len(a) + len(b) + 1):
        candidates = []
        
        for len_a in range(1, min(len(a), total_len) + 1):
            len_b = total_len - len_a
            if len_b < 1 or len_b > len(b):
                continue
                
            for start_a in range(len(a) - len_a + 1):
                sa = a[start_a:start_a + len_a]
                
                for start_b in range(len(b) - len_b + 1):
                    sb = b[start_b:start_b + len_b]
                    
                    for cand in [sa + sb, sb + sa]:
                        if is_palindrome(cand):
                            candidates.append(cand)
        
        if candidates:
            # For same length, pick lexicographically smallest
            candidates.sort()
            if len(candidates[0]) > max_len:
                best = candidates[0]
                max_len = len(candidates[0])

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