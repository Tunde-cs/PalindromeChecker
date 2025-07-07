
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
    
    palindromes = set()  # Use set to avoid duplicates
    
    # Limit substring length to prevent overly long combinations
    # Try smaller substrings first with reasonable limits
    max_substring_len = min(len(a), len(b), 3)  # Limit to 3 chars per substring
    print(f"[DEBUG] Max substring length: {max_substring_len}")
    
    for len_a in range(1, min(len(a), max_substring_len) + 1):
        for start_a in range(len(a) - len_a + 1):
            sa = a[start_a:start_a + len_a]
            
            for len_b in range(1, min(len(b), max_substring_len) + 1):
                for start_b in range(len(b) - len_b + 1):
                    sb = b[start_b:start_b + len_b]
                    
                    # Try both combinations
                    for combo in [sa + sb, sb + sa]:
                        print(f"[DEBUG] Trying combo: '{combo}' (sa='{sa}', sb='{sb}')")
                        if combo == combo[::-1]:  # is palindrome
                            print(f"[DEBUG] Found palindrome: '{combo}'")
                            palindromes.add(combo)
    
    if not palindromes:
        print("[DEBUG] No palindromes found, returning -1")
        return "-1"
    
    print(f"[DEBUG] Found palindromes: {sorted(palindromes)}")
    
    # Sort by: (length DESC, lexicographic ASC)
    sorted_palindromes = sorted(palindromes, key=lambda x: (-len(x), x))
    
    print(f"[DEBUG] Sorted by (length DESC, lex ASC): {sorted_palindromes}")
    
    # Return the longest palindrome, lexicographically smallest if tie
    result = sorted_palindromes[0]
    print(f"[DEBUG] Final result: '{result}' (length: {len(result)})")
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
