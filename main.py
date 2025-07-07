
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
    
    palindromes = set()
    
    # Remove the restrictive length limit - let's explore more possibilities
    max_len = min(len(a), len(b), 10)  # Reasonable limit for performance
    print(f"[DEBUG] Max substring length: {max_len}")
    
    # Try all possible substring combinations
    for len_a in range(1, len(a) + 1):
        for start_a in range(len(a) - len_a + 1):
            sa = a[start_a:start_a + len_a]
            
            for len_b in range(1, len(b) + 1):
                for start_b in range(len(b) - len_b + 1):
                    sb = b[start_b:start_b + len_b]
                    
                    # Try both combinations: sa + sb and sb + sa
                    for combo in [sa + sb, sb + sa]:
                        if len(combo) > 20:  # Performance limit
                            continue
                            
                        print(f"[DEBUG] Trying combo: '{combo}' (sa='{sa}', sb='{sb}')")
                        
                        # Check if palindrome using even/odd approach
                        if is_palindrome_even_odd(combo):
                            print(f"[DEBUG] Found palindrome: '{combo}' (length: {len(combo)})")
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


def is_palindrome_even_odd(s):
    """
    Check if string is palindrome using even/odd length approach
    """
    n = len(s)
    if n == 0:
        return True
    
    # Even length palindrome: center is between two middle characters
    if n % 2 == 0:
        center = n // 2
        left = center - 1
        right = center
    # Odd length palindrome: center is the middle character
    else:
        center = n // 2
        left = center - 1
        right = center + 1
    
    # Expand around center
    while left >= 0 and right < n:
        if s[left] != s[right]:
            return False
        left -= 1
        right += 1
    
    return True


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
