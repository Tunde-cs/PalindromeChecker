
#!/usr/bin/env python3

def is_palindrome(s):
    """Check if a string is a palindrome."""
    return s == s[::-1]

def buildPalindrome(a, b):
    """Find the longest palindromic string by concatenating full strings a and b."""
    # Handle edge cases
    if not a or not b:
        return "-1"
    
    # Only try the two possible concatenations: a+b and b+a
    candidates = [a + b, b + a]
    
    valid_palindromes = []
    for candidate in candidates:
        if is_palindrome(candidate):
            valid_palindromes.append(candidate)
    
    if not valid_palindromes:
        return "-1"
    
    # Return the longest palindrome, or lexicographically smallest if tied
    valid_palindromes.sort(key=lambda x: (-len(x), x))
    return valid_palindromes[0]

# Test the problematic cases
test_cases = [
    ("bac", "bac", "baccab"),
    ("abc", "abc", "abccba"), 
    ("jdfh", "fds", "dfhfd"),
    ("abc", "def", "-1"),
]

print("Testing FULL STRING concatenation approach:")
print("=" * 50)

for a, b, expected in test_cases:
    result = buildPalindrome(a, b)
    status = "✓ PASS" if result == expected else "✗ FAIL"
    print(f"a='{a}', b='{b}' → '{result}' (expected: '{expected}') {status}")
