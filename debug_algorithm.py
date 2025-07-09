
#!/usr/bin/env python3

def is_palindrome(s):
    return s == s[::-1]

def buildPalindrome_debug(a, b, target_case=""):
    print(f"\n🔍 DEBUGGING buildPalindrome for {target_case}")
    print(f"Input: a='{a}', b='{b}'")
    
    if not a or not b:
        print("❌ Empty string detected")
        return "-1"

    best_palindrome = None
    max_length = 0
    all_palindromes = []

    print(f"\n📊 Testing all substring combinations...")
    
    # Get all substrings from both strings
    substrings_a = []
    for i in range(len(a)):
        for j in range(i + 1, len(a) + 1):
            substrings_a.append(a[i:j])
    
    substrings_b = []
    for i in range(len(b)):
        for j in range(i + 1, len(b) + 1):
            substrings_b.append(b[i:j])
    
    print(f"Total substrings from a: {len(substrings_a)}")
    print(f"Total substrings from b: {len(substrings_b)}")
    print(f"Total combinations to test: {len(substrings_a) * len(substrings_b) * 2}")
    
    palindrome_count = 0
    
    # Try all combinations
    for sa in substrings_a:
        for sb in substrings_b:
            candidates = [sa + sb, sb + sa]
            
            for candidate in candidates:
                if is_palindrome(candidate):
                    palindrome_count += 1
                    candidate_length = len(candidate)
                    all_palindromes.append((candidate, candidate_length, sa, sb))
                    
                    if palindrome_count <= 10:  # Show first 10 palindromes found
                        print(f"  Found palindrome #{palindrome_count}: '{candidate}' (len={candidate_length}) from '{sa}' + '{sb}'")
                    
                    # Check if this is better than current best
                    if (candidate_length > max_length or 
                        (candidate_length == max_length and 
                         (best_palindrome is None or candidate < best_palindrome))):
                        
                        old_best = best_palindrome
                        best_palindrome = candidate
                        max_length = candidate_length
                        
                        if old_best != candidate:
                            print(f"  🎯 NEW BEST: '{candidate}' (len={candidate_length})")

    print(f"\n📈 SUMMARY:")
    print(f"Total palindromes found: {palindrome_count}")
    print(f"Best palindrome: '{best_palindrome}' (length={max_length})")
    
    # Show top palindromes by length
    if all_palindromes:
        sorted_palindromes = sorted(all_palindromes, key=lambda x: (-x[1], x[0]))
        print(f"\nTop 5 palindromes by length:")
        for i, (p, length, sa, sb) in enumerate(sorted_palindromes[:5]):
            print(f"  {i+1}. '{p}' (len={length}) from '{sa}' + '{sb}'")
    
    return best_palindrome if best_palindrome else "-1"

# Test the specific failing cases
if __name__ == "__main__":
    # Simple test case first
    print("="*80)
    result = buildPalindrome_debug("zlc", "zdw", "Simple Case")
    print(f"Final result: '{result}' (Expected: 'zlz')")
