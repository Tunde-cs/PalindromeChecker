
#!/bin/python3

import math
import os
import random
import re
import sys


def buildPalindrome(a, b):
    print(f"[DEBUG] Input: a='{a}', b='{b}'")
    if not a or not b:
        print("[DEBUG] Empty string detected, returning -1")
        return "-1"
    
    best_palindromes = []
    
    # Try all possible substrings efficiently
    # Limit substring length to avoid TLE but allow reasonable sizes
    max_len = min(10, len(a), len(b))  # More conservative limit
    print(f"[DEBUG] Max substring length: {max_len}")
    
    for len_a in range(1, min(len(a), max_len) + 1):
        for start_a in range(len(a) - len_a + 1):
            sa = a[start_a:start_a + len_a]
            
            for len_b in range(1, min(len(b), max_len) + 1):
                for start_b in range(len(b) - len_b + 1):
                    sb = b[start_b:start_b + len_b]
                    
                    # Try both combinations
                    for combo in [sa + sb, sb + sa]:
                        print(f"[DEBUG] Trying combo: '{combo}' (sa='{sa}', sb='{sb}')")
                        if combo == combo[::-1]:  # is palindrome
                            print(f"[DEBUG] Found palindrome: '{combo}'")
                            best_palindromes.append(combo)
    
    if not best_palindromes:
        print("[DEBUG] No palindromes found, returning -1")
        return "-1"
    
    # Remove duplicates and sort by length then lexicographically
    best_palindromes = list(set(best_palindromes))
    print(f"[DEBUG] All unique palindromes: {best_palindromes}")
    
    # Prefer palindromes of length 3 or more, but not too long
    meaningful_palindromes = [p for p in best_palindromes if len(p) >= 3]
    if meaningful_palindromes:
        # Sort by length (ascending) then lexicographically
        meaningful_palindromes.sort(key=lambda x: (len(x), x))
        print(f"[DEBUG] Meaningful palindromes (len>=3): {meaningful_palindromes}")
        result = meaningful_palindromes[0]  # Shortest meaningful palindrome
    else:
        # Fall back to longest available
        max_length = max(len(p) for p in best_palindromes)
        longest_palindromes = [p for p in best_palindromes if len(p) == max_length]
        result = min(longest_palindromes)
    
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
