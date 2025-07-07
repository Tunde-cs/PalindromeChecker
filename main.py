#!/bin/python3

import math
import os
import random
import re
import sys

# Debug flag - set to False to disable debug output
DEBUG = True

def debug_print(msg):
    if DEBUG:
        print(msg)

def is_palindrome(s):
    return s == s[::-1]

def buildPalindrome(a, b):
    debug_print(f"DEBUG: Input a='{a}', b='{b}'")

    # Early exit for empty strings
    if not a or not b:
        debug_print("DEBUG: Empty string detected, returning -1")
        return "-1"

    # DP table: dp[i][j][k][l][order] = longest palindrome using a[i:i+k] and b[j:j+l]
    # order: 0 for a_substring + b_substring, 1 for b_substring + a_substring
    dp = {}

    max_len = 0
    best_palindrome = None

    # Performance limits
    max_a_len = min(len(a), 15)
    max_b_len = min(len(b), 15)

    debug_print(f"DEBUG: DP table limits: max_a_len={max_a_len}, max_b_len={max_b_len}")

    # Build DP table from zero
    for a_start in range(len(a)):
        for a_len in range(1, min(max_a_len + 1, len(a) - a_start + 1)):
            for b_start in range(len(b)):
                for b_len in range(1, min(max_b_len + 1, len(b) - b_start + 1)):
                    # Extract substrings
                    sa = a[a_start:a_start + a_len]
                    sb = b[b_start:b_start + b_len]

                    # Try both orders
                    for order in [0, 1]:
                        candidate = sa + sb if order == 0 else sb + sa

                        debug_print(f"DEBUG: DP[{a_start}][{a_len}][{b_start}][{b_len}][{order}] = '{candidate}'")

                        # Store in DP table
                        key = (a_start, a_len, b_start, b_len, order)

                        if is_palindrome(candidate):
                            dp[key] = candidate
                            debug_print(f"DEBUG: Found palindrome: '{candidate}' (length {len(candidate)})")

                            # Update best ONLY if this is strictly longer
                            if len(candidate) > max_len:
                                max_len = len(candidate)
                                best_palindrome = candidate
                                debug_print(f"DEBUG: ✓ NEW BEST: '{best_palindrome}' (length {max_len})")
                            else:
                                debug_print(f"DEBUG: Palindrome '{candidate}' not longer than current best (length {max_len})")
                        else:
                            dp[key] = None

    debug_print(f"DEBUG: DP table size: {len(dp)}")
    debug_print(f"DEBUG: Final result: '{best_palindrome if best_palindrome else '-1'}'")

    return best_palindrome if best_palindrome else "-1"


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