#!/bin/python3

import os
from collections import Counter

def is_palindrome(s):
    """Check if a string is a palindrome."""
    return s == s[::-1]

def can_form_palindrome(char_count):
    """Check if character counts can form a palindrome."""
    odd_count = sum(1 for count in char_count.values() if count % 2 == 1)
    return odd_count <= 1

def build_palindrome_from_chars(char_count):
    """Build lexicographically smallest palindrome from character counts."""
    if not can_form_palindrome(char_count):
        return None

    first_half = []
    middle = ""

    for char in sorted(char_count.keys()):
        count = char_count[char]
        first_half.extend([char] * (count // 2))
        if count % 2 == 1:
            middle = char

    first_half_str = ''.join(first_half)
    return first_half_str + middle + first_half_str[::-1]

def buildPalindrome(a, b):
    """
    Build the longest palindrome from substrings of a and b.
    Tries multiple strategies and returns the longest palindrome,
    or lexicographically smallest if there are ties.
    """
    if not a or not b:
        return "-1"

    all_palindromes = []

    # Strategy 1: Direct concatenation of full strings
    for candidate in [a + b, b + a]:
        if is_palindrome(candidate):
            all_palindromes.append(candidate)

    # Strategy 2: Substring concatenation
    for i in range(len(a)):
        for j in range(i + 1, len(a) + 1):
            sa = a[i:j]
            for k in range(len(b)):
                for l in range(k + 1, len(b) + 1):
                    sb = b[k:l]
                    for candidate in [sa + sb, sb + sa]:
                        if is_palindrome(candidate):
                            all_palindromes.append(candidate)

    # Strategy 3: Character rearrangement (use all available characters)
    combined_chars = Counter(a + b)
    rearrange_result = build_palindrome_from_chars(combined_chars)
    if rearrange_result:
        all_palindromes.append(rearrange_result)

    if not all_palindromes:
        return "-1"

    # Remove duplicates and find the best result
    unique_palindromes = list(set(all_palindromes))

    # Sort by length (descending) then lexicographically (ascending)
    unique_palindromes.sort(key=lambda x: (-len(x), x))

    return unique_palindromes[0]

if __name__ == '__main__':
    if 'OUTPUT_PATH' in os.environ:
        # HackerRank submission environment
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