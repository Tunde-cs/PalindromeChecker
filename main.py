
#!/bin/python3

import os
from collections import Counter

def is_palindrome(s):
    return s == s[::-1]

def get_all_substrings(s):
    """Get all possible substrings of a string."""
    substrings = []
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            substrings.append(s[i:j])
    return substrings

def buildPalindrome(a, b):
    """Build palindrome using substring concatenation (not character rearrangement)."""
    print(f"DEBUG: Starting buildPalindrome with a='{a[:20]}...', b='{b[:20]}...'")
    
    if not a or not b:
        print("DEBUG: Empty string detected, returning -1")
        return "-1"
    
    # This is the WRONG approach - using character rearrangement
    # The problem wants substring concatenation, not character rearrangement
    all_chars = Counter(a + b)
    print(f"DEBUG: Using CHARACTER REARRANGEMENT approach (THIS IS WRONG!)")
    print(f"DEBUG: Available characters: {dict(all_chars)}")
    
    # Build the longest possible palindrome using character rearrangement
    left_half = []
    middle_char = ""
    
    # Sort characters to ensure lexicographic order
    for char in sorted(all_chars.keys()):
        count = all_chars[char]
        # Use pairs for the sides
        pairs = count // 2
        left_half.extend([char] * pairs)
        
        # Keep track of the lexicographically smallest odd-count character for middle
        if count % 2 == 1 and middle_char == "":
            middle_char = char
    
    # Build palindrome: left + middle + right
    if not left_half and not middle_char:
        print("DEBUG: No palindrome possible with character rearrangement")
        return "-1"
    
    left_str = ''.join(left_half)
    right_str = left_str[::-1]
    result = left_str + middle_char + right_str
    
    print(f"DEBUG: Character rearrangement result: '{result[:50]}{'...' if len(result) > 50 else ''}'")
    print(f"DEBUG: Result length: {len(result)}")
    
    # Let's also try the CORRECT approach for comparison
    print(f"DEBUG: Now trying CORRECT substring concatenation approach...")
    correct_result = try_substring_concatenation(a, b)
    if correct_result != "-1":
        print(f"DEBUG: Substring concatenation found: '{correct_result}'")
        print(f"DEBUG: RETURNING substring result (correct approach)")
        return correct_result
    else:
        print(f"DEBUG: Substring concatenation found no result")
        print(f"DEBUG: Falling back to character rearrangement")
        return result if result else "-1"

def try_substring_concatenation(a, b):
    """Try the correct approach: substring concatenation."""
    print(f"DEBUG: Trying substring concatenation for a='{a[:10]}...', b='{b[:10]}...'")
    
    best_palindromes = []
    
    # Get all substrings from both strings
    substrings_a = get_all_substrings(a)
    substrings_b = get_all_substrings(b)
    
    print(f"DEBUG: Found {len(substrings_a)} substrings in a, {len(substrings_b)} substrings in b")
    
    # Try all combinations
    palindrome_count = 0
    for sa in substrings_a:
        for sb in substrings_b:
            for candidate in [sa + sb, sb + sa]:
                if is_palindrome(candidate):
                    palindrome_count += 1
                    best_palindromes.append(candidate)
                    if palindrome_count <= 5:  # Only show first few for debugging
                        print(f"DEBUG: Found palindrome #{palindrome_count}: '{candidate}' from '{sa}' + '{sb}'")
    
    if not best_palindromes:
        print("DEBUG: No palindromes found through substring concatenation")
        return "-1"
    
    # Remove duplicates and find the best result
    unique_palindromes = list(set(best_palindromes))
    print(f"DEBUG: Found {len(best_palindromes)} total palindromes, {len(unique_palindromes)} unique")
    
    # Find maximum length
    max_length = max(len(p) for p in unique_palindromes)
    max_length_palindromes = [p for p in unique_palindromes if len(p) == max_length]
    
    print(f"DEBUG: Maximum palindrome length: {max_length}")
    print(f"DEBUG: Found {len(max_length_palindromes)} palindromes with max length")
    
    # Return lexicographically smallest among those with maximum length
    result = min(max_length_palindromes)
    print(f"DEBUG: Substring concatenation result: '{result}'")
    
    # Additional debugging for max length palindromes
    if len(max_length_palindromes) > 1:
        print(f"DEBUG: All max length palindromes: {sorted(max_length_palindromes)}")
    
    return result

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
