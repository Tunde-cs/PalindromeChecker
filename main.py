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

    # Try all possible substrings from a with all possible substrings from b
    for i in range(len(a)):
        for j in range(i + 1, len(a) + 1):
            substring_a = a[i:j]

            for k in range(len(b)):
                for l in range(k + 1, len(b) + 1):
                    substring_b = b[k:l]

                    # Try both concatenation orders
                    for candidate in [substring_a + substring_b, substring_b + substring_a]:
                        # Check if it's a palindrome
                        if candidate == candidate[::-1]:
                            # Update best if this is longer, or same length but lexicographically smaller
                            if (len(candidate) > max_len or 
                                (len(candidate) == max_len and (best is None or candidate < best))):
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