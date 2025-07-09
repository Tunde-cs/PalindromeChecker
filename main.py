
#!/bin/python3

import os
from collections import Counter

def is_palindrome(s):
    return s == s[::-1]

def get_all_rearrangements(s):
    """Get all unique rearrangements of a string."""
    from itertools import permutations
    return list(set(''.join(p) for p in permutations(s)))

def can_form_palindrome_chars(chars):
    """Check if character counts can form a palindrome."""
    odd_count = sum(1 for count in chars.values() if count % 2 == 1)
    return odd_count <= 1

def build_lexicographically_smallest_palindrome(chars):
    """Build the lexicographically smallest palindrome from character counts."""
    if not can_form_palindrome_chars(chars):
        return None
    
    first_half = []
    middle = ""
    
    for char in sorted(chars.keys()):
        count = chars[char]
        first_half.extend([char] * (count // 2))
        if count % 2 == 1:
            middle = char
    
    first_half_str = ''.join(first_half)
    return first_half_str + middle + first_half_str[::-1]

def buildPalindrome(a, b):
    """Build palindrome using substring extraction + character rearrangement."""
    if not a or not b:
        return "-1"

    best_palindromes = []
    
    # Strategy 1: Direct substring concatenation (original approach)
    for i in range(len(a)):
        for j in range(i + 1, len(a) + 1):
            sa = a[i:j]
            for k in range(len(b)):
                for l in range(k + 1, len(b) + 1):
                    sb = b[k:l]
                    for candidate in [sa + sb, sb + sa]:
                        if is_palindrome(candidate):
                            best_palindromes.append(candidate)
    
    # Strategy 2: Substring extraction + rearrangement
    for i in range(len(a)):
        for j in range(i + 1, len(a) + 1):
            sa = a[i:j]
            for k in range(len(b)):
                for l in range(k + 1, len(b) + 1):
                    sb = b[k:l]
                    
                    # Try rearranging characters from both substrings
                    combined_chars = Counter(sa + sb)
                    palindrome = build_lexicographically_smallest_palindrome(combined_chars)
                    if palindrome:
                        best_palindromes.append(palindrome)

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
