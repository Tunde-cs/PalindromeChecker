#!/bin/python3

import math
import os
import random
import re
import sys

def buildPalindrome(a, b):
    print(f"DEBUG: Starting buildPalindrome with a='{a}', b='{b}'")
    
    if not a or not b:
        print("DEBUG: One or both strings are empty, returning '-1'")
        return "-1"

    def is_palindrome(s):
        result = s == s[::-1]
        print(f"DEBUG: is_palindrome('{s}') = {result}")
        return result

    best_palindrome = None
    max_length = 0
    print(f"DEBUG: Initialized best_palindrome={best_palindrome}, max_length={max_length}")

    n = len(a)
    m = len(b)
    print(f"DEBUG: String lengths: n={n}, m={m}")

    # Try all possible substrings from both strings
    for i in range(n):
        print(f"DEBUG: Outer loop i={i}")
        for j in range(i + 1, n + 1):
            sa = a[i:j]
            print(f"DEBUG: Substring from a: sa='{sa}' (i={i}, j={j})")
            
            for k in range(m):
                print(f"DEBUG: Inner loop k={k}")
                for l in range(k + 1, m + 1):
                    sb = b[k:l]
                    print(f"DEBUG: Substring from b: sb='{sb}' (k={k}, l={l})")

                    # Try both sa + sb and sb + sa
                    for combo in [sa + sb, sb + sa]:
                        print(f"DEBUG: Trying combination: '{combo}'")
                        if is_palindrome(combo):
                            print(f"DEBUG: Found palindrome: '{combo}' (length={len(combo)})")
                            # Check if this is better than current best
                            is_longer = len(combo) > max_length
                            is_same_length_and_smaller = (len(combo) == max_length and 
                                                         (best_palindrome is None or combo < best_palindrome))
                            print(f"DEBUG: Current best: '{best_palindrome}' (length={max_length})")
                            print(f"DEBUG: Is longer? {is_longer}")
                            print(f"DEBUG: Is same length and lexicographically smaller? {is_same_length_and_smaller}")
                            
                            if is_longer or is_same_length_and_smaller:
                                print(f"DEBUG: Updating best: '{best_palindrome}' -> '{combo}'")
                                best_palindrome = combo
                                max_length = len(combo)
                            else:
                                print(f"DEBUG: Keeping current best: '{best_palindrome}'")

    print(f"DEBUG: Final result: best_palindrome='{best_palindrome}'")
    return best_palindrome if best_palindrome else "-1"
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for _ in range(t):
        a = input().strip()
        b = input().strip()

        result = buildPalindrome(a, b)

        fptr.write(result + '\n')

    fptr.close()