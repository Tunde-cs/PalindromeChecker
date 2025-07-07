
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
    
    palindrome_count = {}  # Track frequency of each palindrome
    
    # Try all possible substrings
    max_len = min(len(a), len(b))
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
                            palindrome_count[combo] = palindrome_count.get(combo, 0) + 1
    
    if not palindrome_count:
        print("[DEBUG] No palindromes found, returning -1")
        return "-1"
    
    print(f"[DEBUG] Palindrome frequencies: {palindrome_count}")
    
    # Strategy: Prefer shorter palindromes with higher frequency
    # Sort by: (frequency DESC, length ASC, lexicographic ASC)
    sorted_palindromes = sorted(palindrome_count.keys(), 
                              key=lambda x: (-palindrome_count[x], len(x), x))
    
    print(f"[DEBUG] Sorted by (freq DESC, len ASC, lex ASC): {sorted_palindromes}")
    
    # Return the best palindrome according to our criteria
    result = sorted_palindromes[0]
    print(f"[DEBUG] Final result: '{result}' (freq: {palindrome_count[result]})")
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
