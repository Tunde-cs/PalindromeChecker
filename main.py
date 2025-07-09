
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

    all_palindromes = []

    # Strategy 1: Try all substring combinations
    for sa in get_all_substrings(a):
        for sb in get_all_substrings(b):
            for candidate in [sa + sb, sb + sa]:
                if is_palindrome(candidate):
                    all_palindromes.append(candidate)

    # Strategy 2: Try full string concatenation (backup)
    for candidate in [a + b, b + a]:
        if is_palindrome(candidate):
            all_palindromes.append(candidate)

    if not all_palindromes:
        return "-1"

    # Remove duplicates
    unique_palindromes = list(set(all_palindromes))

    # Find maximum length
    max_length = max(len(p) for p in unique_palindromes)
    
    # Get all palindromes with maximum length
    max_length_palindromes = [p for p in unique_palindromes if len(p) == max_length]
    
    # Return lexicographically smallest among those with maximum length
    return min(max_length_palindromes)

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
