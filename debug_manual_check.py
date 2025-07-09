
#!/usr/bin/env python3

def manual_check(a, b, expected):
    print(f"\nManual check for a='{a}', b='{b}', expected='{expected}'")
    print("=" * 60)
    
    # Check if expected is a palindrome
    is_pal = expected == expected[::-1]
    print(f"Is '{expected}' a palindrome? {is_pal}")
    
    if not is_pal:
        print("❌ Expected result is not a palindrome!")
        return False
    
    # Try to find decomposition
    for i in range(1, len(expected)):
        left = expected[:i]
        right = expected[i:]
        
        if left in a and right in b:
            print(f"✓ Found decomposition: '{left}' (from a) + '{right}' (from b)")
            return True
        elif left in b and right in a:
            print(f"✓ Found decomposition: '{left}' (from b) + '{right}' (from a)")
            return True
    
    print("❌ No valid decomposition found")
    return False

# Check the failing cases
print("MANUAL VERIFICATION OF EXPECTED RESULTS")
print("=" * 60)

# Test case 2
a2 = 'qquhuwqhdswxxrxuzzfhkplwunfagppcoildagktgdarveusju'
b2 = 'jwgzcfabbkoxyjxkatjmpprswkdkobdagwdwxsufeesrvncbsz'
manual_check(a2, b2, 'oozlzoo')

# Test case 8  
a8 = 'zlc'
b8 = 'zdw'
manual_check(a8, b8, 'zlz')
