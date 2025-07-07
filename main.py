
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
    
    # Memoization tables
    memo = {}  # Cache for palindrome checks
    best_palindromes = {}  # Cache for best palindromes found so far
    
    def is_palindrome_memo(s):
        if s not in memo:
            memo[s] = (s == s[::-1])
        return memo[s]
    
    # Dynamic programming approach
    # dp[i][j][k][l] represents the best palindrome using substring a[i:i+k] and b[j:j+l]
    dp = {}
    
    def get_best_palindrome(sa_start, sa_len, sb_start, sb_len, order):
        """
        Get best palindrome for given substring parameters
        order: 0 for sa+sb, 1 for sb+sa
        """
        key = (sa_start, sa_len, sb_start, sb_len, order)
        
        if key in dp:
            return dp[key]
        
        # Extract substrings
        sa = a[sa_start:sa_start + sa_len]
        sb = b[sb_start:sb_start + sb_len]
        
        # Create candidate based on order
        candidate = sa + sb if order == 0 else sb + sa
        
        debug_print(f"DEBUG: DP checking candidate: '{candidate}' (sa='{sa}', sb='{sb}', order={order})")
        
        result = None
        if is_palindrome_memo(candidate):
            result = candidate
            debug_print(f"DEBUG: DP found palindrome: '{candidate}' (length {len(candidate)})")
        
        dp[key] = result
        return result
    
    best_palindrome = None
    max_length = 0
    
    # Reasonable limits for performance
    max_sa_len = min(10, len(a))
    max_sb_len = min(10, len(b))
    
    debug_print(f"DEBUG: Using DP with limits: max_sa_len={max_sa_len}, max_sb_len={max_sb_len}")
    
    # Dynamic programming iteration
    for sa_len in range(1, max_sa_len + 1):
        for sa_start in range(len(a) - sa_len + 1):
            for sb_len in range(1, max_sb_len + 1):
                for sb_start in range(len(b) - sb_len + 1):
                    # Try both orders: sa+sb and sb+sa
                    for order in [0, 1]:
                        candidate = get_best_palindrome(sa_start, sa_len, sb_start, sb_len, order)
                        
                        if candidate:
                            # Update best based on lexicographic preference
                            is_longer = len(candidate) > max_length
                            is_lexicographically_smaller = best_palindrome is None or candidate < best_palindrome
                            
                            debug_print(f"DEBUG: DP comparison:")
                            debug_print(f"  - Current candidate: '{candidate}' (length {len(candidate)})")
                            debug_print(f"  - Current best: '{best_palindrome}' (length {max_length})")
                            debug_print(f"  - Is longer? {is_longer}")
                            debug_print(f"  - Is lexicographically smaller? {is_lexicographically_smaller}")
                            
                            if is_lexicographically_smaller or (candidate == best_palindrome and is_longer):
                                old_best = best_palindrome
                                best_palindrome = candidate
                                max_length = len(candidate)
                                debug_print(f"DEBUG: ✓ DP NEW BEST: '{best_palindrome}' (length {max_length}) - replaced '{old_best}'")
                            else:
                                debug_print(f"DEBUG: ✗ DP palindrome '{candidate}' not better than current best '{best_palindrome}'")
    
    debug_print(f"DEBUG: DP cache stats - memo size: {len(memo)}, dp size: {len(dp)}")
    debug_print(f"DEBUG: Final DP result: '{best_palindrome if best_palindrome else '-1'}'")
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
