
#!/bin/python3

import os

def is_palindrome(s):
    """Check if a string is a palindrome."""
    return s == s[::-1]

def buildPalindrome(a, b):
    """
    Build the longest palindrome from substrings of a and b.
    For ties in length, return the lexicographically smallest palindrome.
    """
    if not a or not b:
        return "-1"

    best_palindrome = None
    max_length = 0

    # Get all substrings from a
    substrings_a = []
    for i in range(len(a)):
        for j in range(i + 1, len(a) + 1):
            substrings_a.append(a[i:j])

    # Get all substrings from b
    substrings_b = []
    for i in range(len(b)):
        for j in range(i + 1, len(b) + 1):
            substrings_b.append(b[i:j])

    # Try all combinations of substrings from a and b
    for sa in substrings_a:
        for sb in substrings_b:
            # Try both concatenation orders
            for candidate in [sa + sb, sb + sa]:
                if is_palindrome(candidate):
                    candidate_length = len(candidate)

                    # Check if this is better than current best
                    if (candidate_length > max_length or 
                        (candidate_length == max_length and 
                         (best_palindrome is None or candidate < best_palindrome))):
                        best_palindrome = candidate
                        max_length = candidate_length

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
