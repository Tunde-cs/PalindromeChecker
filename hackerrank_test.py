
#!/usr/bin/env python3

from main import buildPalindrome

def run_hackerrank_tests():
    """Test against actual HackerRank test cases"""
    
    test_cases = [
        ("ottloictodtdtloloollllyocidyiodttoacoctcdcidcdttyoiilocltacdlydaailaiylcttilld", 
         "jevgfsuujwrunvgvgwpfbknkruvwzgxxgksmexqvxbghfffseuugxkwexhzfbpu", 
         "-1"),
        
        ("qquhuwqhdswxxrxuzzfhkplwunfagppcoildagktgdarveusjuqfistulgbglwmfgzrnyxryetwzhlnfewczmnoozlqatugmd", 
         "jwgzcfabbkoxyjxkatjmpprswkdkobdagwdwxsufeesrvncbszcepigpbzuzoootorzfskcwbqorvw", 
         "oozlzoo"),
        
        ("dczatfarqdkelalxzxillkfdvpfpxabqlngdscrentzamztvvcvrtcm", 
         "bqlizijdwtuyfrxolsysxlfebpolcmqsppmrfkyunydtmwbexsngxhwvroandfqjamzkpttslildlrkjoyrpxugiceahgiakev", 
         "lxsysxl"),
        
        ("kfnfolpcfblpncetyhtrwxkbosccskxbuvcrosavnpxzoeoyyghbbqkflslfkqbbhgyyjj", 
         "qrxpxnloeozxpnvasorcvubxksccsobkxwrthytecnplbfcplofx", 
         "folpcfblpncetyhtrwxkbosccskxbuvcrosavnpxzoeoyyghbbqkflslfkqbbhgyyoeozxpnvasorcvubxksccsobkxwrthytecnplbfcplof"),
        
        ("mlfcpidlqrvngnvttaifcbopnwezesomkxhaiafmvkbjaisyr", 
         "btultpnxbcrmornqumatserhieqggrivouwfnbnghdfall", 
         "rvngnvr"),
        
        ("pb", "kkb", "bkkb"),
        ("rfq", "xzj", "-1"),
        ("zlc", "zdw", "zlz"),
        ("s", "k", "-1"),
        ("w", "d", "-1")
    ]
    
    print("HACKERRANK TEST RESULTS")
    print("=" * 60)
    
    passed = 0
    total = len(test_cases)
    
    for i, (a, b, expected) in enumerate(test_cases, 1):
        print(f"\nTest Case {i}:")
        print(f"a = {a[:50]}{'...' if len(a) > 50 else ''}")
        print(f"b = {b[:50]}{'...' if len(b) > 50 else ''}")
        
        result = buildPalindrome(a, b)
        status = "✓ PASS" if result == expected else "✗ FAIL"
        
        if result == expected:
            passed += 1
            
        print(f"Result:   '{result}'")
        print(f"Expected: '{expected}'")
        print(f"Status:   {status}")
        
        if result != expected:
            print(f"MISMATCH: Got '{result}', expected '{expected}'")
    
    print(f"\n{'=' * 60}")
    print(f"SUMMARY: {passed}/{total} tests passed ({passed/total*100:.1f}%)")
    
    if passed == total:
        print("🎉 ALL TESTS PASSED! Your algorithm is ready for submission!")
    else:
        print(f"❌ {total - passed} tests failed. Algorithm needs adjustment.")

if __name__ == "__main__":
    run_hackerrank_tests()
