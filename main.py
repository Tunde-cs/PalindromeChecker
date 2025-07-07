#!/bin/python3

import math
import os
import random
import re
import sys


def buildPalindrome(a, b):
    print(f"[DEBUG] Input a: '{a}', b: '{b}'")

    if not a or not b:
        print("[DEBUG] One or both strings are empty. Returning '-1'")
        return "-1"

    if not (set(a) & set(b)):
        print("[DEBUG] No common characters between strings. Returning '-1'")
        return "-1"

    def is_palindrome(s):
        return s == s[::-1]

    # Collect all possible palindromes
    palindromes = []

    # Try all combinations of substrings up to 20 chars to avoid TLE
    for len_a in range(1, min(len(a), 20) + 1):
        for len_b in range(1, min(len(b), 20) + 1):
            for start_a in range(len(a) - len_a + 1):
                sa = a[start_a:start_a + len_a]
                for start_b in range(len(b) - len_b + 1):
                    sb = b[start_b:start_b + len_b]
                    for combo in [sa + sb, sb + sa]:
                        print(f"[DEBUG] Trying combo: '{combo}' (sa='{sa}', sb='{sb}')")
                        if is_palindrome(combo):
                            print(f"[DEBUG] Palindrome found: '{combo}'")
                            palindromes.append(combo)

    if not palindromes:
        print("[DEBUG] No palindromes found. Returning '-1'")
        return "-1"

    # Try lexicographically smallest overall first
    palindromes.sort()
    result = palindromes[0]
    
    print(f"[DEBUG] All palindromes: {palindromes}")
    print(f"[DEBUG] Final result: '{result}'")
    return result

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
