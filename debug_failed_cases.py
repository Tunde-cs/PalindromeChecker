
#!/usr/bin/env python3

def manual_debug_case(case_num, a, b, expected, our_result):
    print(f"\n{'='*80}")
    print(f"MANUAL DEBUG - TEST CASE {case_num}")
    print(f"{'='*80}")
    print(f"a = '{a[:50]}{'...' if len(a) > 50 else ''}' (length: {len(a)})")
    print(f"b = '{b[:50]}{'...' if len(b) > 50 else ''}' (length: {len(b)})")
    print(f"Expected: '{expected}' (length: {len(expected)})")
    print(f"Our result: '{our_result}' (length: {len(our_result) if our_result != '-1' else 0})")
    
    # Check if expected is a palindrome
    is_pal = expected == expected[::-1]
    print(f"\nIs expected result a palindrome? {is_pal}")
    
    if not is_pal:
        print("❌ ERROR: Expected result is not a palindrome!")
        return
    
    # Try to find how expected result can be formed
    print(f"\nAnalyzing how '{expected}' could be formed:")
    found_decomposition = False
    
    for i in range(1, len(expected)):
        left = expected[:i]
        right = expected[i:]
        
        left_in_a = left in a
        right_in_b = right in b
        left_in_b = left in b
        right_in_a = right in a
        
        if left_in_a and right_in_b:
            print(f"  ✓ '{left}' (from a) + '{right}' (from b)")
            found_decomposition = True
        elif left_in_b and right_in_a:
            print(f"  ✓ '{left}' (from b) + '{right}' (from a)")
            found_decomposition = True
    
    if not found_decomposition:
        print("  ❌ No valid decomposition found")
    
    # Analyze our result if it's different
    if our_result != expected and our_result != '-1':
        print(f"\nAnalyzing our result '{our_result}':")
        our_is_pal = our_result == our_result[::-1]
        print(f"Is our result a palindrome? {our_is_pal}")
        
        if len(our_result) > len(expected):
            print(f"Our result is LONGER ({len(our_result)} vs {len(expected)})")
        elif len(our_result) < len(expected):
            print(f"Our result is SHORTER ({len(our_result)} vs {len(expected)})")
        else:
            print(f"Same length, but lexicographically different")
            print(f"Our result: '{our_result}'")
            print(f"Expected:   '{expected}'")
            print(f"Ours > Expected: {our_result > expected}")

def main():
    print("MANUAL DEBUG OF FAILED TEST CASES")
    print("=" * 80)
    
    # Test Case 2 - FAILED
    manual_debug_case(2,
        "qquhuwqhdswxxrxuzzfhkplwunfagppcoildagktgdarveusju",
        "jwgzcfabbkoxyjxkatjmpprswkdkobdagwdwxsufeesrvncbsz", 
        "oozlzoo",
        "zoootoooz")
    
    # Test Case 4 - FAILED
    manual_debug_case(4,
        "kfnfolpcfblpncetyhtrwxkbosccskxbuvcrosavnpxzoeoyyg",
        "qrxpxnloeozxpnvasorcvubxksccsobkxwrthytecnplbfcplo",
        "folpcfblpncetyhtrwxkbosccskxbuvcrosavnpxzoeoyyghbbqkflslfkqbbhgyyoeozxpnvasorcvubxksccsobkxwrthytecnplbfcplof",
        "fblpncetyhtrwxkbosccskxbuvcrosavnpxzoeoyyghbbqkflslfkqbbhgyyoeozxpnvasorcvubxksccsobkxwrthytecnplbf")
    
    # Test Case 5 - FAILED  
    manual_debug_case(5,
        "mlfcpidlqrvngnvttaifcbopnwezesomkxhaiafmvkbjaisyr",
        "btultpnxbcrmornqumatserhieqggrivouwfnbnghdfall",
        "rvngnvr", 
        "tvngnvt")

if __name__ == "__main__":
    main()
