
#!/usr/bin/env python3

import time
from main import buildPalindrome

def run_test_case(a, b, expected=None, description=""):
    print(f"\n{'='*60}")
    print(f"TEST: {description}")
    print(f"Input: a='{a}', b='{b}'")
    
    start_time = time.time()
    result = buildPalindrome(a, b)
    elapsed = time.time() - start_time
    
    print(f"Result: '{result}'")
    if expected:
        status = "✓ PASS" if result == expected else "✗ FAIL"
        print(f"Expected: '{expected}' - {status}")
    print(f"Time: {elapsed:.3f}s")
    
    return result

def main():
    print("COMPREHENSIVE TEST SUITE FOR HIDDEN TEST CASES")
    print("=" * 60)
    
    # Basic test cases
    run_test_case("bac", "bac", "aba", "Basic case from problem")
    run_test_case("abc", "def", "-1", "No palindrome possible")
    run_test_case("jdfh", "fds", "dfhfd", "Complex case")
    
    # Edge cases that might be hidden test cases
    run_test_case("", "", "-1", "Both empty strings")
    run_test_case("a", "", "-1", "One empty string")
    run_test_case("", "b", "-1", "Other empty string")
    
    # Single character cases
    run_test_case("a", "a", "aa", "Same single character")
    run_test_case("a", "b", "-1", "Different single characters")
    
    # Identical strings (potential edge case)
    run_test_case("abc", "abc", "abccba", "Identical strings")
    run_test_case("palindrome", "palindrome", None, "Longer identical strings")
    
    # Reverse string cases
    run_test_case("abc", "cba", "abccba", "String and its reverse")
    run_test_case("ab", "ba", "abba", "Short reverse case")
    
    # Cases with repeating characters
    run_test_case("aaa", "aaa", "aaaaaa", "All same character")
    run_test_case("aab", "baa", None, "Repeating with variation")
    
    # Cases that might hit the length limit
    run_test_case("a" * 25, "b" * 25, None, "Long strings (25 chars each)")
    run_test_case("abcdefghijklmnopqrstu", "uvwxyzabcdefghijklmno", None, "20+ char strings")
    
    # Palindrome substrings
    run_test_case("aba", "cdc", None, "Both contain palindromes")
    run_test_case("racecar", "level", None, "Full palindrome inputs")
    
    # Cases with overlapping characters
    run_test_case("abcd", "dcba", "abcddcba", "Perfect complement")
    run_test_case("xyz", "zyx", "xyzyx", "3-char complement")
    
    # Performance test cases
    run_test_case("abcdefghij", "jihgfedcba", None, "10-char performance test")
    
    # Lexicographically smallest preference test
    run_test_case("ba", "ab", "abba", "Lexicographic preference test")
    run_test_case("cab", "bac", "aba", "Multiple same-length palindromes")
    
    # Cases with no common characters
    run_test_case("xyz", "abc", "-1", "No common characters")
    run_test_case("123", "456", "-1", "No overlap at all")
    
    print(f"\n{'='*60}")
    print("TEST SUITE COMPLETE")

if __name__ == "__main__":
    main()
