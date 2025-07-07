
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
    best = None
    max_len = 0
    max_limit = 20  # Performance limit
    
    debug_print(f"DEBUG: Input a='{a}', b='{b}'")
    
    # Early exit for empty strings
    if not a or not b:
        debug_print("DEBUG: Empty string detected, returning -1")
        return "-1"
    
    debug_print(f"DEBUG: Max substring length limit: {min(len(a), max_limit)} for a, {min(len(b), max_limit)} for b")
    
    total_combinations = 0
    palindromes_found = 0
    
    for len_a in range(1, min(len(a), max_limit) + 1):
        for start_a in range(len(a) - len_a + 1):
            sa = a[start_a:start_a + len_a]

            for len_b in range(1, min(len(b), max_limit) + 1):
                # Early termination only if we can't possibly beat current best
                if best and len_a + len_b <= max_len:
                    continue
                    
                for start_b in range(len(b) - len_b + 1):
                    sb = b[start_b:start_b + len_b]
                    
                    debug_print(f"DEBUG: Trying combo: sa='{sa}' sb='{sb}'")
                    total_combinations += 1
                    
                    for cand in [sa + sb, sb + sa]:
                        debug_print(f"DEBUG: Testing candidate: '{cand}'")
                        if is_palindrome(cand):
                            palindromes_found += 1
                            debug_print(f"DEBUG: Found palindrome: '{cand}' (length {len(cand)})")
                            
                            if len(cand) > max_len or (len(cand) == max_len and (best is None or cand < best)):
                                old_best = best
                                best = cand
                                max_len = len(cand)
                                debug_print(f"DEBUG: New best: '{best}' (length {max_len}) - replaced '{old_best}'")
                            else:
                                debug_print(f"DEBUG: Palindrome '{cand}' not better than current best '{best}'")
                        else:
                            debug_print(f"DEBUG: '{cand}' is not a palindrome")
    
    debug_print(f"DEBUG: Total combinations tested: {total_combinations}")
    debug_print(f"DEBUG: Palindromes found: {palindromes_found}")
    debug_print(f"DEBUG: Final result: '{best if best else '-1'}'")
    
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
