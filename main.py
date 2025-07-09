#!/bin/python3

import os

def is_palindrome(s):
    """Check if a string is a palindrome."""
    return s == s[::-1]

def buildPalindrome(a, b):
    """
    Build the longest palindrome from substrings of a and b.
    Returns the lexicographically smallest if there are ties.
    """
    if not a or not b:
        return "-1"

    best_palindrome = None
    max_length = 0

    # Try all possible substrings from both strings
    # For each substring from 'a', try combining with each substring from 'b'
    for i in range(len(a)):
        for j in range(i + 1, len(a) + 1):
            substring_a = a[i:j]

            for k in range(len(b)):
                for l in range(k + 1, len(b) + 1):
                    substring_b = b[k:l]

                    # Try both orders: a+b and b+a
                    candidates = [substring_a + substring_b, substring_b + substring_a]

                    for candidate in candidates:
                        if is_palindrome(candidate):
                            # Check if this is better than current best
                            if (len(candidate) > max_length or 
                                (len(candidate) == max_length and (best_palindrome is None or candidate < best_palindrome))):
                                best_palindrome = candidate
                                max_length = len(candidate)

    return best_palindrome if best_palindrome else "-1"

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