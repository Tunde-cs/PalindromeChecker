#!/bin/python3

import os

def is_palindrome(s):
    """Check if a string is a palindrome."""
    return s == s[::-1]

def get_all_substrings(s):
    """Get all possible substrings of a string."""
    return [s[i:j] for i in range(len(s)) for j in range(i + 1, len(s) + 1)]

def buildPalindrome(a, b):
    """Find the longest palindromic string using substring concatenation only."""
    if not a or not b:
        return "-1"

    best_palindromes = []

    # Strategy 1: Try all substring combinations (ONLY this strategy)
    # This should be the primary and often only way to form palindromes
    for sa in get_all_substrings(a):
        for sb in get_all_substrings(b):
            for candidate in [sa + sb, sb + sa]:
                if is_palindrome(candidate):
                    best_palindromes.append(candidate)

    # Strategy 2: Try full string concatenation (backup)
    for candidate in [a + b, b + a]:
        if is_palindrome(candidate):
            best_palindromes.append(candidate)

    if not best_palindromes:
        return "-1"

    # Remove duplicates and find the best result
    unique_palindromes = list(set(best_palindromes))

    # Sort by length (descending) then lexicographically (ascending)
    unique_palindromes.sort(key=lambda x: (-len(x), x))

    return unique_palindromes[0]

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