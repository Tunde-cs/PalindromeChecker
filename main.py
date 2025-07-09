
#!/bin/python3

import os

def is_palindrome(s):
    """Check if a string is a palindrome."""
    return s == s[::-1]

def buildPalindrome(a, b):
    """
    Build the longest palindrome from substrings of a and b.
    For ties, prefer palindromes formed by longer substrings first, then lexicographically smallest.
    """
    if not a or not b:
        return "-1"

    candidates = []

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
                    # Store candidate with metadata for better tie-breaking
                    candidates.append({
                        'palindrome': candidate,
                        'length': len(candidate),
                        'min_substring_len': min(len(sa), len(sb)),
                        'max_substring_len': max(len(sa), len(sb)),
                        'substring_len_sum': len(sa) + len(sb)
                    })

    if not candidates:
        return "-1"

    # Find the maximum length
    max_length = max(c['length'] for c in candidates)
    max_length_candidates = [c for c in candidates if c['length'] == max_length]
    
    # For ties, use a more sophisticated comparison:
    # 1. Prefer longer minimum substring length
    # 2. If still tied, prefer longer maximum substring length  
    # 3. If still tied, prefer lexicographically smallest palindrome
    def tie_breaker(candidate):
        return (
            -candidate['min_substring_len'],  # Prefer longer min substring (negative for desc order)
            -candidate['max_substring_len'],  # Prefer longer max substring
            candidate['palindrome']           # Lexicographically smallest
        )
    
    best_candidate = min(max_length_candidates, key=tie_breaker)
    return best_candidate['palindrome']

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
