#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import combinations

def buildPalindrome(a, b):
    best = "-1"
    max_len = 0
    n, m = len(a), len(b)

    # Early exit for empty strings
    if not a or not b:
        return "-1"

    # Arms from a, right arm from b (positions not required to be contiguous)
    for a_start in range(n):
        for a_end in range(a_start + 1, n + 1):
            left_arm = a[a_start:a_end]
            rev_left = left_arm[::-1]
            arm_len = len(left_arm)
            if arm_len > m:
                continue
            # Try all possible subsets of positions in b of length arm_len
            for b_indices in combinations(range(m), arm_len):
                right_candidate = ''.join(b[i] for i in b_indices)
                if right_candidate == rev_left:
                    center = ''.join(b[i] for i in range(m) if i not in b_indices)
                    pal = left_arm + center + rev_left
                    if len(pal) > max_len or (len(pal) == max_len and (best == "-1" or pal < best)):
                        best = pal
                        max_len = len(pal)

    # Arms from b, right arm from a (positions not required to be contiguous)
    for b_start in range(m):
        for b_end in range(b_start + 1, m + 1):
            left_arm = b[b_start:b_end]
            rev_left = left_arm[::-1]
            arm_len = len(left_arm)
            if arm_len > n:
                continue
            for a_indices in combinations(range(n), arm_len):
                right_candidate = ''.join(a[i] for i in a_indices)
                if right_candidate == rev_left:
                    center = ''.join(a[i] for i in range(n) if i not in a_indices)
                    pal = left_arm + center + rev_left
                    if len(pal) > max_len or (len(pal) == max_len and (best == "-1" or pal < best)):
                        best = pal
                        max_len = len(pal)

    return best

if __name__ == '__main__':
    t = int(input())
    for case in range(t):
        a = input().strip()
        b = input().strip()
        result = buildPalindrome(a, b)
        print(result)