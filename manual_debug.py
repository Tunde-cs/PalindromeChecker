
#!/usr/bin/env python3

from main import buildPalindrome

def manual_debug_case(case_name, a, b, expected):
    print(f"\n{'='*80}")
    print(f"MANUAL DEBUG: {case_name}")
    print(f"{'='*80}")
    print(f"Input: a = '{a}'")
    print(f"Input: b = '{b}'")
    print(f"Expected: '{expected}'")
    
    # Test our algorithm
    result = buildPalindrome(a, b, debug=True)
    print(f"\nOur result: '{result}'")
    print(f"Status: {'✓ PASS' if result == expected else '✗ FAIL'}")
    
    if result != expected:
        print(f"\n🔍 ANALYZING THE MISMATCH:")
        print(f"Expected: '{expected}' (len={len(expected)})")
        print(f"Got:      '{result}' (len={len(result) if result != '-1' else 0})")
        
        # Check if expected is actually a palindrome
        is_expected_palindrome = expected == expected[::-1]
        print(f"Is expected result a palindrome? {is_expected_palindrome}")
        
        # Check if expected can be formed from the inputs
        print(f"\n📝 CHECKING IF EXPECTED CAN BE FORMED:")
        expected_formed = False
        for split in range(1, len(expected)):
            left = expected[:split]
            right = expected[split:]
            
            if left in a and right in b:
                print(f"  ✓ '{expected}' = '{left}' (from a) + '{right}' (from b)")
                expected_formed = True
                break
            elif left in b and right in a:
                print(f"  ✓ '{expected}' = '{left}' (from b) + '{right}' (from a)")
                expected_formed = True
                break
        
        if not expected_formed:
            print(f"  ✗ Cannot form '{expected}' from direct substrings")
            
        # Check if our result is valid
        if result != '-1':
            is_our_palindrome = result == result[::-1]
            print(f"\n🔍 CHECKING OUR RESULT:")
            print(f"Is our result a palindrome? {is_our_palindrome}")
            
            # Try to find how our result was formed
            our_formed = False
            for split in range(1, len(result)):
                left = result[:split]
                right = result[split:]
                
                if left in a and right in b:
                    print(f"  ✓ Our '{result}' = '{left}' (from a) + '{right}' (from b)")
                    our_formed = True
                    break
                elif left in b and right in a:
                    print(f"  ✓ Our '{result}' = '{left}' (from b) + '{right}' (from a)")
                    our_formed = True
                    break
            
            if not our_formed:
                print(f"  ✗ Cannot verify how our result was formed")
        
        # Compare lengths and lexicographical order
        print(f"\n📊 COMPARISON:")
        if result != '-1':
            print(f"Length comparison: expected={len(expected)}, our={len(result)}")
            if len(expected) == len(result):
                print(f"Lexicographical: expected < our = {expected < result}")
            elif len(expected) > len(result):
                print(f"Expected is longer - should be preferred")
            else:
                print(f"Our result is longer - should be preferred")

# Debug the 2 failing cases
print("MANUAL DEBUGGING OF FAILED TEST CASES")
print("=" * 80)

# Failing Case 1: Test Case 2 (renumbered)
manual_debug_case(
    "Test Case 2",
    "dczatfarqdkelalxzxillkfdvpfpxabqlngdscrentzamztvvcvrtcm",
    "bqlizijdwtuyfrxolsysxlfebpolcmqsppmrfkyunydtmwbexsngxhwvroandfqjamzkpttslildlrkjoyrpxugiceahgiakev",
    "lxsysxl"
)

# Failing Case 2: Test Case 7  
manual_debug_case(
    "Test Case 7",
    "zlc",
    "zdw", 
    "zlz"
)

print(f"\n{'='*80}")
print("MANUAL DEBUGGING COMPLETE")
