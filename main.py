
#!/bin/python3

import math
import os
import random
import re
import sys

def buildPalindrome(a, b):
    if not a or not b:
        return "-1"
    
    best = None
    max_len = 0
    
    # Generate all substrings from both strings
    subs_a = []
    subs_b = []
    
    for i in range(len(a)):
        for j in range(i + 1, len(a) + 1):
            subs_a.append(a[i:j])
    
    for i in range(len(b)):
        for j in range(i + 1, len(b) + 1):
            subs_b.append(b[i:j])
    
    # Try direct concatenations: sa + sb and sb + sa
    for sa in subs_a:
        for sb in subs_b:
            for candidate in [sa + sb, sb + sa]:
                if candidate == candidate[::-1]:
                    if len(candidate) > max_len or (len(candidate) == max_len and (best is None or candidate < best)):
                        best = candidate
                        max_len = len(candidate)
    
    # Try three-part combinations where middle can be from either string
    # Format: part_from_one_string + middle + part_from_other_string
    all_subs = subs_a + subs_b
    
    for sa in subs_a:
        for middle in all_subs:
            for sb in subs_b:
                if len(sa) + len(middle) + len(sb) > 10:  # Performance limit
                    continue
                candidate = sa + middle + sb
                if candidate == candidate[::-1]:
                    if len(candidate) > max_len or (len(candidate) == max_len and (best is None or candidate < best)):
                        best = candidate
                        max_len = len(candidate)
    
    # Try with middle from string b and sides from string a
    for sb in subs_b:
        for middle in all_subs:
            for sa in subs_a:
                if len(sb) + len(middle) + len(sa) > 10:  # Performance limit
                    continue
                candidate = sb + middle + sa
                if candidate == candidate[::-1]:
                    if len(candidate) > max_len or (len(candidate) == max_len and (best is None or candidate < best)):
                        best = candidate
                        max_len = len(candidate)

    return best if best else "-1"

if __name__ == '__main__':
    t = int(input())
    for case in range(t):
        a = input().strip()
        b = input().strip()
        result = buildPalindrome(a, b)
        print(result)
