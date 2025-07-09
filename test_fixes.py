
#!/usr/bin/env python3

from main import buildPalindrome

def test_specific_cases():
    print("TESTING SPECIFIC FAILING CASES")
    print("=" * 50)
    
    # Test Case 4 - We're getting shorter result than expected
    print("\n🔍 TEST CASE 4:")
    a4 = "kfnfolpcfblpncetyhtrwxkbosccskxbuvcrosavnpxzoeoyyg"
    b4 = "qrxpxnloeozxpnvasorcvubxksccsobkxwrthytecnplbfcplo"
    expected4 = "folpcfblpncetyhtrwxkbosccskxbuvcrosavnpxzoeoyyghbbqkflslfkqbbhgyyoeozxpnvasorcvubxksccsobkxwrthytecnplbfcplof"
    
    print(f"a = '{a4[:30]}...' (len={len(a4)})")
    print(f"b = '{b4[:30]}...' (len={len(b4)})")
    print(f"Expected: '{expected4[:50]}...' (len={len(expected4)})")
    
    result4 = buildPalindrome(a4, b4, debug=True)
    print(f"Got:      '{result4[:50] if result4 != '-1' else result4}{'...' if len(result4) > 50 else ''}' (len={len(result4) if result4 != '-1' else 0})")
    
    status4 = "✓ PASS" if result4 == expected4 else "✗ FAIL"
    print(f"Status: {status4}")
    
    # Test Case 5 - Same length but lexicographically different
    print("\n🔍 TEST CASE 5:")
    a5 = "mlfcpidlqrvngnvttaifcbopnwezesomkxhaiafmvkbjaisyr"
    b5 = "btultpnxbcrmornqumatserhieqggrivouwfnbnghdfall"
    expected5 = "rvngnvr"
    
    print(f"a = '{a5[:30]}...' (len={len(a5)})")
    print(f"b = '{b5[:30]}...' (len={len(b5)})")
    print(f"Expected: '{expected5}' (len={len(expected5)})")
    
    result5 = buildPalindrome(a5, b5, debug=True)
    print(f"Got:      '{result5}' (len={len(result5) if result5 != '-1' else 0})")
    
    status5 = "✓ PASS" if result5 == expected5 else "✗ FAIL"
    print(f"Status: {status5}")
    
    if result5 != expected5 and result5 != '-1':
        print(f"Lexicographic comparison: '{result5}' < '{expected5}' = {result5 < expected5}")
    
    # Test some basic cases to ensure we didn't break anything
    print("\n🔍 BASIC VERIFICATION:")
    basic_cases = [
        ("bac", "bac", "baccab"),
        ("jdfh", "fds", "dfhfd"),
        ("abc", "def", "-1"),
    ]
    
    for a, b, expected in basic_cases:
        result = buildPalindrome(a, b)
        status = "✓ PASS" if result == expected else "✗ FAIL"
        print(f"'{a}' + '{b}' → '{result}' (expected: '{expected}') {status}")

if __name__ == "__main__":
    test_specific_cases()
