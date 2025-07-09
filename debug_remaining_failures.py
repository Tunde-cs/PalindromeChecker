
#!/usr/bin/env python3

from main import buildPalindrome

def debug_case(case_num, a, b, expected):
    print(f"\n{'='*60}")
    print(f"DEBUGGING TEST CASE {case_num}")
    print(f"a = '{a[:50]}{'...' if len(a) > 50 else ''}'")
    print(f"b = '{b[:50]}{'...' if len(b) > 50 else ''}'")
    print(f"Expected: '{expected}' (len={len(expected)})")
    
    result = buildPalindrome(a, b, debug=True)
    print(f"Got:      '{result}' (len={len(result) if result != '-1' else 0})")
    
    status = "✓ PASS" if result == expected else "✗ FAIL"
    print(f"Status: {status}")
    
    # Manual verification of expected result
    print(f"\nVerifying expected result '{expected}':")
    print(f"Is palindrome: {expected == expected[::-1]}")
    
    # Check if expected can be formed
    for split in range(1, len(expected)):
        left = expected[:split]
        right = expected[split:]
        if left in a and right in b:
            print(f"✓ Can form as: '{left}' (from a) + '{right}' (from b)")
            break
        elif left in b and right in a:
            print(f"✓ Can form as: '{left}' (from b) + '{right}' (from a)")
            break
    else:
        print(f"✗ Cannot form '{expected}' from direct substrings")

# Test the remaining failing cases
failing_cases = [
    (3, "dczatfarqdkelalxzxillkfdvpfpxabqlngdscrentzamztvvcvrtcm", 
        "bqlizijdwtuyfrxolsysxlfebpolcmqsppmrfkyunydtmwbexsngxhwvroandfqjamzkpttslildlrkjoyrpxugiceahgiakev", 
        "lxsysxl"),
    (8, "zlc", "zdw", "zlz")
]

for case_num, a, b, expected in failing_cases:
    debug_case(case_num, a, b, expected)
