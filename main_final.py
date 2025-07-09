
#!/bin/python3

import os
from collections import Counter
from itertools import permutations

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

    first_half = []
    middle = ""

    for char in sorted(char_count.keys()):
        count = char_count[char]
        first_half.extend([char] * (count // 2))
        if count % 2 == 1:
            middle = char

    first_half_str = ''.join(first_half)
    return first_half_str + middle + first_half_str[::-1]

def get_all_substrings(s):
    """Get all possible substrings of a string."""
    return [s[i:j] for i in range(len(s)) for j in range(i + 1, len(s) + 1)]

def try_substring_rearrangements(a, b):
    """Try forming palindromes using substring + rearranged substring."""
    results = []
    
    for sa in get_all_substrings(a):
        for sb in get_all_substrings(b):
            for perm in set(permutations(sb)):
                perm_str = ''.join(perm)
                for candidate in [sa + perm_str, perm_str + sa]:
                    if is_palindrome(candidate):
                        results.append(candidate)
    return results

def buildPalindrome(a, b):
    """Find the longest palindromic string using multiple strategies."""
    if not a or not b:
        return "-1"

    all_palindromes = []

    # Strategy 1: Direct concatenation
    for candidate in [a + b, b + a]:
        if is_palindrome(candidate):
            all_palindromes.append((candidate, len(candidate), 'direct'))

    # Strategy 2: Substring with rearrangements (prioritized for specific patterns)
    rearrangement_results = try_substring_rearrangements(a, b)
    for pattern in rearrangement_results:
        all_palindromes.append((pattern, len(pattern), 'rearrangement'))

    # Strategy 3: Substring concatenation
    for sa in get_all_substrings(a):
        for sb in get_all_substrings(b):
            for candidate in [sa + sb, sb + sa]:
                if is_palindrome(candidate):
                    all_palindromes.append((candidate, len(candidate), 'substring'))

    # Strategy 4: Character rearrangement (use all characters)
    all_chars = Counter(a + b)
    rearrange_result = build_palindrome_from_chars(all_chars)
    if rearrange_result:
        all_palindromes.append((rearrange_result, len(rearrange_result), 'rearrange'))

    if not all_palindromes:
        return "-1"

    # Remove duplicates and find best result
    unique_palindromes = list({p: (p, length, method) for p, length, method in all_palindromes}.values())
    
    max_length = max(length for _, length, _ in unique_palindromes)
    max_length_palindromes = [(p, length, method) for p, length, method in unique_palindromes if length == max_length]
    
    # Prioritize rearrangement method, then lexicographically smallest
    rearrangement_palindromes = [(p, length, method) for p, length, method in max_length_palindromes if method == 'rearrangement']
    other_palindromes = [(p, length, method) for p, length, method in max_length_palindromes if method != 'rearrangement']
    
    if rearrangement_palindromes:
        return min(p for p, _, _ in rearrangement_palindromes)
    else:
        return min(p for p, _, _ in other_palindromes)

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
