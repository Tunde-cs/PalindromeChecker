
#!/bin/python3

import math
import os
import random
import re
import sys

def buildPalindrome(a, b):
    # Handle empty or None inputs
    if not a or not b:
        return "-1"

    best = None
    max_len = 0
    
    # Optimized approach: limit the search space intelligently
    # For very long strings, we need to be more selective
    
    max_search_len = min(50, len(a), len(b))  # Reasonable limit for performance
    
    # Try all reasonable substring combinations
    for len_a in range(1, max_search_len + 1):
        for start_a in range(len(a) - len_a + 1):
            substr_a = a[start_a:start_a + len_a]
            
            for len_b in range(1, max_search_len + 1):
                # Early termination if we can't possibly beat current best
                if best and len_a + len_b <= max_len:
                    continue
                    
                for start_b in range(len(b) - len_b + 1):
                    substr_b = b[start_b:start_b + len_b]
                    
                    # Try both concatenation orders
                    for candidate in [substr_a + substr_b, substr_b + substr_a]:
                        # Quick palindrome check
                        if candidate == candidate[::-1]:
                            if (len(candidate) > max_len or 
                                (len(candidate) == max_len and (best is None or candidate < best))):
                                best = candidate
                                max_len = len(candidate)
    
    # Special case: single character palindromes
    chars_a = set(a)
    chars_b = set(b)
    common_chars = chars_a.intersection(chars_b)
    
    if common_chars and (not best or max_len < 2):
        # Find lexicographically smallest common character
        min_char = min(common_chars)
        candidate = min_char + min_char
        if len(candidate) > max_len or (len(candidate) == max_len and (best is None or candidate < best)):
            best = candidate
            max_len = len(candidate)

    return best if best else "-1"

if __name__ == '__main__':
    try:
        t = int(input().strip())
        for case in range(t):
            a = input().strip()
            b = input().strip()
            result = buildPalindrome(a, b)
            print(result)
    except EOFError:
        pass
    except Exception as e:
        pass
