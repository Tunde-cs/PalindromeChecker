
#!/usr/bin/env python3

from main import buildPalindrome

def debug_case(a, b, expected, case_name):
    print(f"\n{'='*60}")
    print(f"DEBUGGING {case_name}")
    print(f"a = {a}")
    print(f"b = {b}")
    print(f"Expected: '{expected}'")
    
    # Let's manually check if the expected result can be formed
    print(f"\nAnalyzing expected result '{expected}':")
    print(f"Length: {len(expected)}")
    print(f"Is palindrome: {expected == expected[::-1]}")
    
    # Try to find how expected result could be formed
    for i in range(1, len(expected)):
        left = expected[:i]
        right = expected[i:]
        
        left_in_a = left in a
        right_in_b = right in b
        left_in_b = left in b
        right_in_a = right in a
        
        if left_in_a and right_in_b:
            print(f"  ✓ Can form as: '{left}' (from a) + '{right}' (from b)")
        elif left_in_b and right_in_a:
            print(f"  ✓ Can form as: '{left}' (from b) + '{right}' (from a)")
    
    # Run our algorithm
    result = buildPalindrome(a, b)
    print(f"\nOur result: '{result}'")
    print(f"Length: {len(result) if result != '-1' else 0}")
    
    if result != expected:
        print(f"❌ MISMATCH: Expected '{expected}', got '{result}'")
        
        # Compare lengths
        if result != '-1' and len(result) != len(expected):
            print(f"Length difference: our={len(result)}, expected={len(expected)}")
        
        # If same length, check lexicographic order
        if result != '-1' and len(result) == len(expected):
            print(f"Same length, lexicographic comparison: '{result}' vs '{expected}'")
            print(f"Our result comes first: {result < expected}")
    else:
        print("✅ CORRECT")

# Debug the failing cases
debug_case(
    "qquhuwqhdswxxrxuzzfhkplwunfagppcoildagktgdarveusjuqfistulgbglwmfgzrnyxryetwzhlnfewczmnoozlqatugmd",
    "jwgzcfabbkoxyjxkatjmpprswkdkobdagwdwxsufeesrvncbszcepigpbzuzoootorzfskcwbqorvw",
    "oozlzoo",
    "TEST CASE 2"
)

debug_case(
    "dczatfarqdkelalxzxillkfdvpfpxabqlngdscrentzamztvvcvrtcm",
    "bqlizijdwtuyfrxolsysxlfebpolcmqsppmrfkyunydtmwbexsngxhwvroandfqjamzkpttslildlrkjoyrpxugiceahgiakev",
    "lxsysxl",
    "TEST CASE 3"
)

debug_case(
    "zlc",
    "zdw",
    "zlz",
    "TEST CASE 8"
)
