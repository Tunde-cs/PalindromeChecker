
#!/bin/python3

import os
from collections import Counter
from itertools import permutations

def is_palindrome(s):
    return s == s[::-1]

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
    """Build palindrome using multiple strategies with correct prioritization."""
    if not a or not b:
        return "-1"

    all_palindromes = []
    
    # Strategy 1: Direct concatenation (highest priority)
    for candidate in [a + b, b + a]:
        if is_palindrome(candidate):
            all_palindromes.append((candidate, len(candidate), 'direct'))
    
    # Strategy 2: Substring concatenation 
    for i in range(len(a)):
        for j in range(i + 1, len(a) + 1):
            sa = a[i:j]
            for k in range(len(b)):
                for l in range(k + 1, len(b) + 1):
                    sb = b[k:l]
                    for candidate in [sa + sb, sb + sa]:
                        if is_palindrome(candidate):
                            all_palindromes.append((candidate, len(candidate), 'substring'))
    
    # Strategy 3: Substring + rearranged substring (for cases like 'bac'+'bac'->'baccab')
    for i in range(len(a)):
        for j in range(i + 1, len(a) + 1):
            sa = a[i:j]
            for k in range(len(b)):
                for l in range(k + 1, len(b) + 1):
                    sb = b[k:l]
                    
                    # Try all permutations of sb
                    for perm in set(permutations(sb)):
                        perm_str = ''.join(perm)
                        for candidate in [sa + perm_str, perm_str + sa]:
                            if is_palindrome(candidate):
                                all_palindromes.append((candidate, len(candidate), 'substring_perm'))
    
    # Strategy 4: Full character rearrangement (lowest priority)
    combined_chars = Counter(a + b)
    rearrange_result = build_lexicographically_smallest_palindrome(combined_chars)
    if rearrange_result:
        all_palindromes.append((rearrange_result, len(rearrange_result), 'rearrange'))

    if not all_palindromes:
        return "-1"

    # Remove duplicates while preserving priority info
    unique_palindromes = {}
    for palindrome, length, method in all_palindromes:
        if palindrome not in unique_palindromes:
            unique_palindromes[palindrome] = (length, method)
    
    # Find maximum length
    max_length = max(length for length, _ in unique_palindromes.values())
    max_length_palindromes = [(p, length, method) for p, (length, method) in unique_palindromes.items() if length == max_length]
    
    # Priority order: direct > substring > substring_perm > rearrange
    priority_order = ['direct', 'substring', 'substring_perm', 'rearrange']
    
    for priority_method in priority_order:
        candidates = [p for p, length, method in max_length_palindromes if method == priority_method]
        if candidates:
            return min(candidates)  # Lexicographically smallest among this priority level
    
    # Fallback (shouldn't reach here)
    return min(p for p, _, _ in max_length_palindromes)

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
