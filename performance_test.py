
#!/usr/bin/env python3

import time
from main import buildPalindrome

def performance_test():
    print("PERFORMANCE TESTING")
    print("=" * 50)
    
    # Test cases with increasing complexity
    test_cases = [
        ("a" * 10, "b" * 10, "Large different chars"),
        ("abc" * 5, "cba" * 5, "Repeated patterns"),
        ("abcdefghij", "jihgfedcba", "Perfect reverses"),
        ("a" * 20, "a" * 20, "Max length same chars"),
        ("abcdefghijklmnopqrst", "tsrqponmlkjihgfedcba", "20-char reverses"),
    ]
    
    for a, b, description in test_cases:
        print(f"\nTest: {description}")
        print(f"Input lengths: a={len(a)}, b={len(b)}")
        
        start_time = time.time()
        result = buildPalindrome(a, b)
        elapsed = time.time() - start_time
        
        print(f"Result: '{result[:50]}{'...' if len(result) > 50 else ''}'")
        print(f"Output length: {len(result) if result != '-1' else 0}")
        print(f"Time: {elapsed:.3f}s")
        
        if elapsed > 1.0:
            print("⚠️  WARNING: Slow performance detected!")

if __name__ == "__main__":
    performance_test()
