
#!/usr/bin/env python3

from main import buildPalindrome

def test_case_8():
    a = 'zlc'
    b = 'zdw'
    expected = 'zlz'
    
    print(f"Testing: a='{a}', b='{b}'")
    print(f"Expected: '{expected}'")
    
    result = buildPalindrome(a, b, debug=True)
    print(f"Got: '{result}'")
    
    print(f"\nStatus: {'✓ PASS' if result == expected else '✗ FAIL'}")

if __name__ == "__main__":
    test_case_8()
