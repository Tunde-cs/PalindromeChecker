
#!/usr/bin/env python3

from main import find_all_palindromes, buildPalindrome

def analyze_case(a, b, expected, case_name):
    print(f"\n{'='*80}")
    print(f"ANALYZING {case_name}")
    print(f"a = {a[:50]}{'...' if len(a) > 50 else ''}")
    print(f"b = {b[:50]}{'...' if len(b) > 50 else ''}")
    print(f"Expected: '{expected}'")
    
    # Check if expected is valid
    print(f"Expected length: {len(expected)}")
    print(f"Expected is palindrome: {expected == expected[::-1]}")
    
    # Find all palindromes our algorithm can create
    all_palindromes = find_all_palindromes(a, b, max_limit=30)
    
    print(f"\nTotal palindromes found: {len(all_palindromes)}")
    
    # Show top 10 longest palindromes
    print(f"\nTop 10 longest palindromes we can create:")
    for i, p in enumerate(all_palindromes[:10]):
        marker = " ← EXPECTED" if p == expected else ""
        print(f"  {i+1:2d}. '{p}' (len={len(p)}){marker}")
    
    # Check if expected palindrome is in our list
    if expected in all_palindromes:
        index = all_palindromes.index(expected) + 1
        print(f"\n✓ Expected result IS in our list at position #{index}")
    else:
        print(f"\n✗ Expected result NOT found in our palindromes")
        
        # Try to manually check if expected can be formed
        print(f"\nManually checking if '{expected}' can be formed:")
        for split in range(1, len(expected)):
            left = expected[:split]
            right = expected[split:]
            
            if left in a and right in b:
                print(f"  ✓ Can form as: '{left}' (from a) + '{right}' (from b)")
                break
            elif left in b and right in a:
                print(f"  ✓ Can form as: '{left}' (from b) + '{right}' (from a)")
                break
        else:
            print(f"  ✗ Cannot form '{expected}' from substrings")
    
    # Our result
    our_result = buildPalindrome(a, b)
    print(f"\nOur result: '{our_result}'")
    print(f"Match: {'✓ PASS' if our_result == expected else '✗ FAIL'}")

# Test the failing cases
failing_cases = [
    # Case 2
    ("qquhuwqhdswxxrxuzzfhkplwunfagppcoildagktgdarveusju", 
     "jwgzcfabbkoxyjxkatjmpprswkdkobdagwdwxsufeesrvncbsz", 
     "oozlzoo", "Case 2"),
    
    # Case 5  
    ("mlfcpidlqrvngnvttaifcbopnwezesomkxhaiafmvkbjaisyr",
     "btultpnxbcrmornqumatserhieqggrivouwfnbnghdfall",
     "rvngnvr", "Case 5"),
]

for a, b, expected, name in failing_cases:
    analyze_case(a, b, expected, name)

print(f"\n{'='*80}")
print("ANALYSIS COMPLETE")
