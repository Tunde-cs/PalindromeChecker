
#!/bin/python3

import os

def is_palindrome(s):
    """Check if a string is a palindrome."""
    return s == s[::-1]

def get_all_substrings(s):
    """Get all possible substrings of a string."""
    return [s[i:j] for i in range(len(s)) for j in range(i + 1, len(s) + 1)]

def buildPalindrome(a, b):
    """Find the longest palindromic string using substring concatenation first."""
    if not a or not b:
        return "-1"
    
    best_palindromes = []
    
    # Strategy 1: Try all substring combinations (this should find 'baccab')
    for sa in get_all_substrings(a):
        for sb in get_all_substrings(b):
            for candidate in [sa + sb, sb + sa]:
                if is_palindrome(candidate):
                    best_palindromes.append(candidate)
    
    # Strategy 2: Try full string concatenation
    for candidate in [a + b, b + a]:
        if is_palindrome(candidate):
            best_palindromes.append(candidate)
    
    # Strategy 3: Character rearrangement (only if no substring solutions found)
    if not best_palindromes:
        from collections import Counter
        
        def can_form_palindrome(char_count):
            odd_count = sum(1 for count in char_count.values() if count % 2 == 1)
            return odd_count <= 1
        
        def build_palindrome_from_chars(char_count):
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
        
        # Try character rearrangement for all characters
        all_chars = Counter(a + b)
        rearrange_result = build_palindrome_from_chars(all_chars)
        if rearrange_result:
            best_palindromes.append(rearrange_result)
        
        # Try character rearrangement for substring combinations
        for sa in get_all_substrings(a):
            for sb in get_all_substrings(b):
                combined_chars = Counter(sa + sb)
                subset_result = build_palindrome_from_chars(combined_chars)
                if subset_result:
                    best_palindromes.append(subset_result)
    
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
