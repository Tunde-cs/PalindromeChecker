
#!/bin/python3

import math
import os
import random
import re
import sys

def buildPalindrome(a, b):
    print(f"DEBUG: Input a='{a}', b='{b}'", file=sys.stderr)
    
    best = None
    max_len = 0
    n, m = len(a), len(b)
    palindromes_found = []

    if not a or not b:
        print(f"DEBUG: Empty string detected, returning -1", file=sys.stderr)
        return "-1"

    print(f"DEBUG: Starting search with strings of length {n} and {m}", file=sys.stderr)

    # Try all possible substring combinations from both strings
    for i in range(n):
        for j in range(i + 1, n + 1):
            sa = a[i:j]
            
            for k in range(m):
                for l in range(k + 1, m + 1):
                    sb = b[k:l]
                    
                    # Try both concatenation orders
                    candidates = [sa + sb, sb + sa]
                    
                    for candidate in candidates:
                        if candidate == candidate[::-1]:
                            palindromes_found.append(candidate)
                            print(f"DEBUG: Found palindrome '{candidate}' (len={len(candidate)}) from sa='{sa}' + sb='{sb}'", file=sys.stderr)
                            
                            if len(candidate) > max_len or (len(candidate) == max_len and (best is None or candidate < best)):
                                old_best = best
                                best = candidate
                                max_len = len(candidate)
                                print(f"DEBUG: New best palindrome: '{best}' (replaced '{old_best}')", file=sys.stderr)

    print(f"DEBUG: Total palindromes found: {len(palindromes_found)}", file=sys.stderr)
    if palindromes_found:
        print(f"DEBUG: All palindromes: {sorted(set(palindromes_found))}", file=sys.stderr)
        print(f"DEBUG: Final best: '{best}' with length {max_len}", file=sys.stderr)
    else:
        print(f"DEBUG: No palindromes found, returning -1", file=sys.stderr)

    return best if best else "-1"

if __name__ == '__main__':
    print(f"DEBUG: Starting program", file=sys.stderr)
    t = int(input())
    print(f"DEBUG: Processing {t} test cases", file=sys.stderr)
    
    for case in range(t):
        print(f"DEBUG: Test case {case + 1}/{t}", file=sys.stderr)
        a = input().strip()
        b = input().strip()
        result = buildPalindrome(a, b)
        print(result)
        print(f"DEBUG: Test case {case + 1} result: '{result}'", file=sys.stderr)
