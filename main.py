
#!/bin/python3

import math
import os
import random
import re
import sys

def buildPalindrome(a, b):
    if not a or not b:
        return "-1"
    
    palindrome_count = {}  # Track frequency of each palindrome
    
    # Try all possible substrings
    max_len = min(len(a), len(b))
    
    for len_a in range(1, min(len(a), max_len) + 1):
        for start_a in range(len(a) - len_a + 1):
            sa = a[start_a:start_a + len_a]
            
            for len_b in range(1, min(len(b), max_len) + 1):
                for start_b in range(len(b) - len_b + 1):
                    sb = b[start_b:start_b + len_b]
                    
                    # Try both combinations
                    for combo in [sa + sb, sb + sa]:
                        if combo == combo[::-1]:  # is palindrome
                            palindrome_count[combo] = palindrome_count.get(combo, 0) + 1
    
    if not palindrome_count:
        return "-1"
    
    # Get unique palindromes
    unique_palindromes = list(palindrome_count.keys())
    
    # Sort by: (length DESC, lexicographic ASC)
    sorted_palindromes = sorted(unique_palindromes, 
                              key=lambda x: (-len(x), x))
    
    # Return the longest palindrome, lexicographically smallest if tie
    return sorted_palindromes[0]

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
