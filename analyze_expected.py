
#!/usr/bin/env python3

def analyze_palindrome_formation(a, b, expected):
    """Analyze how the expected palindrome could be formed"""
    print(f"\nAnalyzing: a='{a}', b='{b}', expected='{expected}'")
    print("=" * 50)
    
    # Check if expected is actually a palindrome
    is_palindrome = expected == expected[::-1]
    print(f"Is '{expected}' a palindrome? {is_palindrome}")
    
    if not is_palindrome:
        print("ERROR: Expected result is not even a palindrome!")
        return
    
    # Try to find ANY way to form the expected palindrome
    print(f"\nTrying to decompose '{expected}' into parts from a='{a}' and b='{b}':")
    
    expected_len = len(expected)
    found_valid_decomposition = False
    
    # Try all possible split points
    for split in range(1, expected_len):
        left = expected[:split]
        right = expected[split:]
        
        # Check if left is in a and right is in b (or vice versa)
        left_in_a = left in a
        right_in_b = right in b
        left_in_b = left in b  
        right_in_a = right in a
        
        if left_in_a and right_in_b:
            print(f"  ✓ Found: '{left}' (from a) + '{right}' (from b)")
            found_valid_decomposition = True
        elif left_in_b and right_in_a:
            print(f"  ✓ Found: '{left}' (from b) + '{right}' (from a)")
            found_valid_decomposition = True
    
    if not found_valid_decomposition:
        print("  ✗ No valid decomposition found using direct substrings")
        
        # Check if it could be formed by rearranging characters
        from collections import Counter
        a_chars = Counter(a)
        b_chars = Counter(b)
        expected_chars = Counter(expected)
        
        print(f"\nCharacter analysis:")
        print(f"  Available from a: {dict(a_chars)}")
        print(f"  Available from b: {dict(b_chars)}")
        print(f"  Required for expected: {dict(expected_chars)}")
        
        # Check if we have enough characters
        all_available = a_chars + b_chars
        can_form = all(all_available[char] >= expected_chars[char] for char in expected_chars)
        print(f"  Can form '{expected}' by rearranging all available characters? {can_form}")

# Test the failing cases
analyze_palindrome_formation('bac', 'bac', 'baccab')
analyze_palindrome_formation('abc', 'abc', 'abccba')

# Test a working case for comparison
analyze_palindrome_formation('jdfh', 'fds', 'dfhfd')
