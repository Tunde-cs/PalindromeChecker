
#!/usr/bin/env python3

from collections import Counter

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
    
    # Build first half of palindrome
    first_half = []
    middle = ""
    
    # Sort characters to ensure lexicographically smallest result
    for char in sorted(char_count.keys()):
        count = char_count[char]
        # Add half of each character's count to first half
        first_half.extend([char] * (count // 2))
        # If count is odd, save one for middle
        if count % 2 == 1:
            middle = char  # Only one odd count allowed for palindrome
    
    # Build palindrome: first_half + middle + reversed_first_half
    first_half_str = ''.join(first_half)
    palindrome = first_half_str + middle + first_half_str[::-1]
    
    return palindrome

def buildPalindrome(a, b):
    """Find the longest palindromic string by rearranging characters from a and b."""
    # Handle edge cases
    if not a or not b:
        return "-1"
    
    # Count all available characters
    all_chars = Counter(a + b)
    
    # Try to form palindrome using all characters
    palindrome = build_palindrome_from_chars(all_chars)
    
    if palindrome:
        return palindrome
    else:
        return "-1"

# Test the problematic cases
test_cases = [
    ("bac", "bac", "baccab"),
    ("abc", "abc", "abccba"), 
    ("jdfh", "fds", "dfhfd"),
    ("abc", "def", "-1"),
]

print("Testing CHARACTER REARRANGEMENT approach:")
print("=" * 50)

for a, b, expected in test_cases:
    result = buildPalindrome(a, b)
    status = "✓ PASS" if result == expected else "✗ FAIL"
    print(f"a='{a}', b='{b}' → '{result}' (expected: '{expected}') {status}")
    
    # Show character analysis
    all_chars = Counter(a + b)
    print(f"  Available chars: {dict(all_chars)}")
    if result != "-1":
        result_chars = Counter(result)
        print(f"  Result uses: {dict(result_chars)}")
    print()
