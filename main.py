#!/bin/python3

import os

def is_palindrome(s):
    return s == s[::-1]

def buildPalindrome(a, b):
    """Build palindrome using substring concatenation approach."""
    if not a or not b:
        return "-1"

    best_palindromes = []

    # Try all possible substring combinations
    for i in range(len(a)):
        for j in range(i + 1, len(a) + 1):
            sa = a[i:j]

            for k in range(len(b)):
                for l in range(k + 1, len(b) + 1):
                    sb = b[k:l]

                    # Try both concatenation orders
                    for candidate in [sa + sb, sb + sa]:
                        if is_palindrome(candidate):
                            best_palindromes.append(candidate)

    if not best_palindromes:
        return "-1"

    # Find longest palindromes
    max_length = max(len(p) for p in best_palindromes)
    longest_palindromes = [p for p in best_palindromes if len(p) == max_length]

    # Return lexicographically smallest among longest
    return min(longest_palindromes)

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