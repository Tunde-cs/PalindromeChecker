
#!/usr/bin/env python3

def is_palindrome(s):
    return s == s[::-1]

def buildPalindrome_debug(a, b):
    """Debug version that shows all combinations being tested"""
    print(f"\nDEBUG: Testing a='{a}', b='{b}'")
    
    if not a or not b:
        print("DEBUG: Empty string detected, returning -1")
        return "-1"

    best = None
    max_len = 0
    all_palindromes = []

    # Try all possible substring combinations
    for len_a in range(1, len(a) + 1):
        for start_a in range(len(a) - len_a + 1):
            sa = a[start_a:start_a + len_a]

            for len_b in range(1, len(b) + 1):
                for start_b in range(len(b) - len_b + 1):
                    sb = b[start_b:start_b + len_b]

                    # Try both concatenation orders
                    candidates = [sa + sb, sb + sa]
                    for candidate in candidates:
                        if is_palindrome(candidate):
                            print(f"DEBUG: Found palindrome '{candidate}' from '{sa}' + '{sb}'")
                            all_palindromes.append((candidate, len(candidate), sa, sb))
                            
                            cand_len = len(candidate)
                            if (cand_len > max_len or 
                                (cand_len == max_len and (best is None or candidate < best))):
                                print(f"DEBUG: New best palindrome: '{candidate}' (length {cand_len})")
                                best = candidate
                                max_len = cand_len

    print(f"DEBUG: All palindromes found: {sorted(all_palindromes, key=lambda x: (-x[1], x[0]))}")
    print(f"DEBUG: Final result: '{best}' (length {max_len})")
    return best if best else "-1"

# Test the failing cases
print("DEBUGGING FAILING TEST CASES")
print("=" * 50)

# Case 1: bac + bac should return 'baccab', but returns 'aba'
result1 = buildPalindrome_debug("bac", "bac")
print(f"Result: '{result1}', Expected: 'baccab'")

print("\n" + "=" * 50)

# Case 2: abc + abc should return 'abccba', but returns 'aba'  
result2 = buildPalindrome_debug("abc", "abc")
print(f"Result: '{result2}', Expected: 'abccba'")
