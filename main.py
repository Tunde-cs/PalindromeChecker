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
                    center = ''.join(b[i] for i in range(m)
                                     if i not in b_indices)
                    if left_arm == 'ooz' and right_candidate == 'zoo':
                        print(f"HIT: left_arm='ooz' from a[{a_start}:{a_end}], right_arm='zoo' from b{b_indices}, center='{center}'")
                    print(
                        f"Trying left_arm='{left_arm}' from a[{a_start}:{a_end}], right_arm='{right_candidate}' from b{b_indices}, center='{center}'"
                    )
                    pal = left_arm + center + rev_left
                    if pal == pal[::-1]:
                        if len(pal) > max_len or (len(pal) == max_len
                                                  and pal > best):
                            print(
                                f"Palindrome: '{pal}' left_arm from a[{a_start}:{a_end}]='{left_arm}', center from b[other indices]='{center}', right_arm from b{b_indices}='{right_candidate}'"
                            )
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
                    center = ''.join(a[i] for i in range(n)
                                     if i not in a_indices)
                    pal = left_arm + center + rev_left
                    if pal == pal[::-1]:
                        if len(pal) > max_len or (len(pal) == max_len
                                                  and pal > best):
                            print(
                                f"Palindrome: '{pal}' left_arm from b[{b_start}:{b_end}]='{left_arm}', center from a[other indices]='{center}', right_arm from a{a_indices}='{right_candidate}'"
                            )
                            best = pal
                            max_len = len(pal)

    print(f"FINAL BEST: '{best}'\n")
    return best


if __name__ == '__main__':
    t = int(input())
    for case in range(t):
        a = input().strip()
        b = input().strip()
        print(f"==== TEST CASE {case+1} ====")
        print(f"a = '{a}', b = '{b}'")
        result = buildPalindrome(a, b)
        print(result)
