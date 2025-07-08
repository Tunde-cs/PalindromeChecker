

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
    
    # Get all substrings from both strings
    subs_a = set()
    subs_b = set()
    
    for i in range(len(a)):
        for j in range(i + 1, len(a) + 1):
            subs_a.add(a[i:j])
    
    for i in range(len(b)):
        for j in range(i + 1, len(b) + 1):
            subs_b.add(b[i:j])
    
    # Try all possible combinations
    all_subs = list(subs_a) + list(subs_b)
    
    # Try simple concatenations first
    for sa in subs_a:
        for sb in subs_b:
            for candidate in [sa + sb, sb + sa]:
                if candidate == candidate[::-1]:
                    if len(candidate) > max_len or (len(candidate) == max_len and (best is None or candidate < best)):
                        best = candidate
                        max_len = len(candidate)
    
    # Try three-part combinations: part1 + part2 + part3
    # where parts can come from either string
    for part1 in all_subs:
        if len(part1) > 4:  # Reasonable limit
            continue
        for part2 in all_subs:
            if len(part1) + len(part2) > 5:
                continue
            for part3 in all_subs:
                if len(part1) + len(part2) + len(part3) > 8:
                    continue
                
                candidate = part1 + part2 + part3
                if candidate == candidate[::-1]:
                    # Verify that we're using substrings from both original strings
                    if (part1 in subs_a or part2 in subs_a or part3 in subs_a) and \
                       (part1 in subs_b or part2 in subs_b or part3 in subs_b):
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

