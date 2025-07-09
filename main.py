
#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

def is_palindrome(s):
    """Check if a string is a palindrome."""
    return s == s[::-1]

def can_form_palindrome(char_count):
    """Check if given character counts can form a palindrome."""
    odd_count = sum(1 for count in char_count.values() if count % 2 == 1)
    return odd_count <= 1

def build_palindrome_from_chars(char_count):
    """Build the lexicographically smallest palindrome from character counts."""
    if not can_form_palindrome(char_count):
        return None
    
    # Build first half of palindrome
    first_half = []
    middle = ""
    
    # Sort characters in normal order to ensure lexicographically smallest result
    for char in sorted(char_count.keys()):
        count = char_count[char]
        # Add half of each character's count to first half
        first_half.extend([char] * (count // 2))
        # If count is odd, save one for middle
        if count % 2 == 1:
            middle = char  # Only one odd count allowed for palindrome
    
    # Build palindrome: first_half + middle + reversed_first_half
    first_half_str = ''.join(first_half)
    palindrome = first_half_str + middle + first_half_str[::-1]
    
    return palindrome

def get_all_substrings(s):
    """Get all possible substrings of a string."""
    substrings = []
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            substrings.append(s[i:j])
    return substrings

def try_substring_with_rearrangements(a, b):
    """Try to form palindromes using substrings from a and rearrangements of substrings from b."""
    from itertools import permutations
    all_palindromes = []
    
    # Key insight: "baccab" = "bac" (from a) + "cab" (rearrangement of "bac" from b)
    # For each substring from a, try all rearrangements of substrings from b
    
    for start_a in range(len(a)):
        for end_a in range(start_a + 1, len(a) + 1):
            sa = a[start_a:end_a]
            
            for start_b in range(len(b)):
                for end_b in range(start_b + 1, len(b) + 1):
                    sb = b[start_b:end_b]
                    
                    # Try all permutations of sb
                    for perm in set(permutations(sb)):
                        perm_str = ''.join(perm)
                        
                        # Try both concatenation orders: sa + perm_str and perm_str + sa
                        for candidate in [sa + perm_str, perm_str + sa]:
                            if is_palindrome(candidate) and len(candidate) <= 20:
                                # Verify we have the required characters
                                required = Counter(candidate)
                                available = Counter(a + b)
                                
                                if all(available[c] >= required[c] for c in required):
                                    all_palindromes.append(candidate)
    
    return list(set(all_palindromes))  # Remove duplicates

def buildPalindrome(a, b):
    """Find the longest palindromic string using multiple strategies."""
    # Handle edge cases
    if not a or not b:
        return "-1"
    
    all_palindromes = []
    
    # STRATEGY 1: Substring concatenation (all possible combinations)
    for sa in get_all_substrings(a):
        for sb in get_all_substrings(b):
            for candidate in [sa + sb, sb + sa]:
                if is_palindrome(candidate):
                    all_palindromes.append((candidate, len(candidate), 'substring'))
    
    # STRATEGY 2: Character rearrangement (use all characters)
    all_chars = Counter(a + b)
    rearrange_result = build_palindrome_from_chars(all_chars)
    if rearrange_result:
        all_palindromes.append((rearrange_result, len(rearrange_result), 'rearrange'))
    
    # STRATEGY 3: Substring with rearrangements approach (key for baccab case)
    rearrangement_results = try_substring_with_rearrangements(a, b)
    for pattern in rearrangement_results:
        all_palindromes.append((pattern, len(pattern), 'rearrangement'))
    
    if not all_palindromes:
        return "-1"
    
    # Remove duplicates
    unique_palindromes = []
    seen = set()
    for p, length, method in all_palindromes:
        if p not in seen:
            unique_palindromes.append((p, length, method))
            seen.add(p)
    
    # Sort by length (descending), then lexicographically (ascending)
    unique_palindromes.sort(key=lambda x: (-x[1], x[0]))
    
    return unique_palindromes[0][0]

if __name__ == '__main__':
    if 'OUTPUT_PATH' in os.environ:
        # Submission environment
        fptr = open(os.environ['OUTPUT_PATH'], 'w')
        t = int(input().strip())

        for _ in range(t):
            a = input().strip()
            b = input().strip()
            result = buildPalindrome(a, b)
            fptr.write(result + '\n')

        fptr.close()
    else:
        # Local testing
        t = int(input().strip())

        for _ in range(t):
            a = input().strip()
            b = input().strip()
            result = buildPalindrome(a, b)
            print(result)
