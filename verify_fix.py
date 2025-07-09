
#!/usr/bin/env python3

from main import buildPalindrome

def test_critical_cases():
    """Test the cases that were previously failing"""
    
    test_cases = [
        # Basic functionality
        ("bac", "bac", "baccab"),
        ("abc", "abc", "abccba"), 
        ("jdfh", "fds", "dfhfd"),
        
        # Edge cases
        ("abc", "def", "-1"),
        ("", "", "-1"),
        ("a", "a", "aa"),
        
        # Lexicographic preference
        ("ba", "ab", "abba"),  # Should prefer "abba" over "baab"
        
        # Complex cases
        ("race", "car", "racecar"),
        ("abcd", "dcba", "abcddcba"),
    ]
    
    print("VERIFICATION OF FIXED ALGORITHM")
    print("=" * 50)
    
    passed = 0
    total = len(test_cases)
    
    for i, (a, b, expected) in enumerate(test_cases):
        result = buildPalindrome(a, b)
        status = "✓ PASS" if result == expected else "✗ FAIL"
        
        print(f"Test {i+1}: a='{a}', b='{b}'")
        print(f"  Expected: '{expected}'")
        print(f"  Got:      '{result}' {status}")
        
        if result == expected:
            passed += 1
        else:
            # Debug the failing case
            print(f"  DEBUG: Analyzing failure...")
            debug_result = buildPalindrome(a, b, debug=True)
        
        print()
    
    print(f"SUMMARY: {passed}/{total} tests passed")
    return passed == total

if __name__ == "__main__":
    test_critical_cases()
