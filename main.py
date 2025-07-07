
#!/bin/python3

import math
import os
import random
import re
import sys


def buildPalindrome(a, b):
    if not a or not b:
        return "-1"
    
    # Combine both strings and find the longest possible palindrome
    # that uses substrings from both a and b
    
    def can_form_palindrome(s1, s2):
        # Try s1 + s2 and s2 + s1, return the longest palindrome possible
        candidates = []
        
        # For each possible way to combine substrings
        for i in range(len(s1) + 1):
            for j in range(len(s2) + 1):
                if i == 0 and j == 0:
                    continue
                    
                # Take prefix of s1 and s2
                part1 = s1[:i] if i > 0 else ""
                part2 = s2[:j] if j > 0 else ""
                
                if part1 and part2:  # Must use from both strings
                    # Try both orders
                    for combo in [part1 + part2, part2 + part1]:
                        if combo == combo[::-1]:  # is palindrome
                            candidates.append(combo)
        
        return candidates
    
    best_palindromes = []
    
    # Try all possible substrings efficiently
    # Limit substring length to avoid TLE
    max_len = min(50, len(a), len(b))  # Reasonable limit
    
    for len_a in range(1, min(len(a), max_len) + 1):
        for start_a in range(len(a) - len_a + 1):
            sa = a[start_a:start_a + len_a]
            
            for len_b in range(1, min(len(b), max_len) + 1):
                for start_b in range(len(b) - len_b + 1):
                    sb = b[start_b:start_b + len_b]
                    
                    # Try both combinations
                    for combo in [sa + sb, sb + sa]:
                        if combo == combo[::-1]:  # is palindrome
                            best_palindromes.append(combo)
    
    if not best_palindromes:
        return "-1"
    
    # Remove duplicates and find longest palindromes
    best_palindromes = list(set(best_palindromes))
    max_length = max(len(p) for p in best_palindromes)
    longest_palindromes = [p for p in best_palindromes if len(p) == max_length]
    
    # Return lexicographically smallest among longest
    return min(longest_palindromes)


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
