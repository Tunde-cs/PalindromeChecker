
#!/bin/python3

import math
import os
import random
import re
import sys
import time

#
# Complete the 'buildPalindrome' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#


def is_palindrome(s):
    return s == s[::-1]

def buildPalindrome(a, b):
    print(f"DEBUG: Processing strings a='{a}' (len={len(a)}), b='{b}' (len={len(b)})")
    start_time = time.time()
    
    best = None
    max_len = 0
    max_limit = 20  # Adjusted for performance
    total_combinations = 0
    palindromes_found = 0
    
    print(f"DEBUG: Max substring length limit: {min(len(a), max_limit)} for a, {min(len(b), max_limit)} for b")
    
    for len_a in range(1, min(len(a), max_limit) + 1):
        print(f"DEBUG: Testing substrings of length {len_a} from string a")
        
        for start_a in range(len(a) - len_a + 1):
            sa = a[start_a:start_a + len_a]
            
            # Progress update every 10 iterations for longer strings
            if start_a % 10 == 0 and len(a) > 20:
                elapsed = time.time() - start_time
                print(f"DEBUG: Progress - len_a={len_a}, start_a={start_a}/{len(a)-len_a}, elapsed={elapsed:.2f}s")

            for len_b in range(1, min(len(b), max_limit) + 1):
                for start_b in range(len(b) - len_b + 1):
                    sb = b[start_b:start_b + len_b]
                    total_combinations += 2  # Testing both sa+sb and sb+sa
                    
                    for cand in [sa + sb, sb + sa]:
                        if is_palindrome(cand):
                            palindromes_found += 1
                            print(f"DEBUG: Found palindrome '{cand}' (len={len(cand)}) from sa='{sa}' + sb='{sb}'")
                            
                            if len(cand) > max_len or (len(cand) == max_len and (best is None or cand < best)):
                                print(f"DEBUG: New best palindrome: '{cand}' (replacing '{best}')")
                                best = cand
                                max_len = len(cand)
    
    elapsed = time.time() - start_time
    print(f"DEBUG: Total combinations tested: {total_combinations}")
    print(f"DEBUG: Palindromes found: {palindromes_found}")
    print(f"DEBUG: Total processing time: {elapsed:.3f}s")
    print(f"DEBUG: Final result: '{best}' (len={len(best) if best else 0})")
    print("DEBUG: ---")
    
    return best if best else "-1"


if __name__ == '__main__':
    # Check if we're in testing environment or actual submission
    if 'OUTPUT_PATH' in os.environ:
        # Actual submission environment
        fptr = open(os.environ['OUTPUT_PATH'], 'w')
        t = int(input().strip())

        for case_num in range(t):
            print(f"DEBUG: Processing test case {case_num + 1}/{t}")
            a = input().strip()
            b = input().strip()
            result = buildPalindrome(a, b)
            fptr.write(result + '\n')

        fptr.close()
    else:
        # Local testing environment
        print("DEBUG: Running in local test mode")
        test_cases = [
            ("bac", "bac"),    # Expected: aba
            ("abc", "def"),    # Expected: -1
            ("jdfh", "fds"),   # Expected: dfhfd
        ]

        for i, (a, b) in enumerate(test_cases):
            print(f"DEBUG: Test case {i+1}/{len(test_cases)}")
            result = buildPalindrome(a, b)
            print(f"Result for a='{a}', b='{b}': {result}")
            print()
