
#!/usr/bin/env python3

from main import buildPalindrome

def debug_test_case(case_num, a, b, expected):
    print(f"\n{'='*80}")
    print(f"DEBUGGING TEST CASE {case_num}")
    print(f"a = '{a[:50]}{'...' if len(a) > 50 else ''}' (length: {len(a)})")
    print(f"b = '{b[:50]}{'...' if len(b) > 50 else ''}' (length: {len(b)})")
    print(f"Expected: '{expected}' (length: {len(expected)})")
    print(f"{'='*80}")
    
    result = buildPalindrome(a, b, debug=True)
    
    print(f"\nFINAL RESULT: '{result}' (length: {len(result) if result != '-1' else 0})")
    print(f"Expected:     '{expected}' (length: {len(expected)})")
    
    if result == expected:
        print("✅ MATCH")
    else:
        print("❌ MISMATCH")
        if result != '-1' and expected != '-1':
            if len(result) != len(expected):
                print(f"Length difference: got {len(result)}, expected {len(expected)}")
            elif len(result) == len(expected):
                print(f"Same length but different lexicographic choice")

# Test the failing cases
if __name__ == "__main__":
    # Test Case 2 (failing)
    debug_test_case(2, 
        "qquhuwqhdswxxrxuzzfhkplwunfagppcoildagktgdarveusju",
        "jwgzcfabbkoxyjxkatjmpprswkdkobdagwdwxsufeesrvncbsz",
        "oozlzoo")
    
    # Test Case 8 (failing) 
    debug_test_case(8,
        "zlc",
        "zdw", 
        "zlz")
