
#!/usr/bin/env python3

from main import buildPalindrome

def debug_test_case_4():
    a = 'mlfcpidlqrvngnvttaifcbopnwezesomkxhaiafmvkbjaisyr'
    b = 'btultpnxbcrmornqumatserhieqggrivouwfnbnghdfall'
    expected = 'rvngnvr'
    
    print("="*80)
    print("DEBUGGING TEST CASE 4")
    print("="*80)
    print(f"a = {a}")
    print(f"b = {b}")
    print(f"Expected: '{expected}'")
    
    # Check if expected can be formed
    print(f"\nChecking if '{expected}' can be formed:")
    for split in range(1, len(expected)):
        left = expected[:split]
        right = expected[split:]
        
        left_in_a = left in a
        right_in_b = right in b
        left_in_b = left in b
        right_in_a = right in a
        
        if left_in_a and right_in_b:
            print(f"  ✓ '{left}' (from a) + '{right}' (from b)")
        elif left_in_b and right_in_a:
            print(f"  ✓ '{left}' (from b) + '{right}' (from a)")
    
    # Run our algorithm with debug
    print(f"\nRunning our algorithm with debug:")
    result = buildPalindrome(a, b, debug=True)
    print(f"\nOur result: '{result}'")
    print(f"Expected:   '{expected}'")
    
    print(f"\nComparison:")
    print(f"'{result}' > '{expected}' = {result > expected}")
    print(f"Our result length: {len(result)}")
    print(f"Expected length:   {len(expected)}")

if __name__ == "__main__":
    debug_test_case_4()
