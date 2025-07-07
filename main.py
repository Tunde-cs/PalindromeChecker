
#!/bin/python3

import math
import os
import random
import re
import sys

def buildPalindrome(a, b):
    if not a or not b:
        return "-1"
    
    best_palindrome = None
    best_length = 0
    
    # Limit search space for performance
    max_len = min(20, len(a), len(b))
    
    # Try substrings in order of decreasing length for early termination
    for total_len in range(min(len(a) + len(b), 40), 0, -1):
        if best_palindrome and total_len <= best_length:
            break  # Can't find better palindrome
            
        # Try all combinations that sum to total_len
        for len_a in range(1, min(total_len, len(a), max_len) + 1):
            len_b = total_len - len_a
            if len_b < 1 or len_b > len(b) or len_b > max_len:
                continue
                
            candidates = []
            
            # Generate all substrings of length len_a from a
            for start_a in range(len(a) - len_a + 1):
                sa = a[start_a:start_a + len_a]
                
                # Generate all substrings of length len_b from b
                for start_b in range(len(b) - len_b + 1):
                    sb = b[start_b:start_b + len_b]
                    
                    # Check both combinations
                    for combo in [sa + sb, sb + sa]:
                        if combo == combo[::-1]:  # is palindrome
                            candidates.append(combo)
            
            if candidates:
                # Sort candidates lexicographically and take the smallest
                candidates.sort()
                best_candidate = candidates[0]
                
                if len(best_candidate) > best_length:
                    best_palindrome = best_candidate
                    best_length = len(best_candidate)
                elif len(best_candidate) == best_length and (best_palindrome is None or best_candidate < best_palindrome):
                    best_palindrome = best_candidate
    
    return best_palindrome if best_palindrome else "-1"

if __name__ == '__main__':
    # Handle both submission environment and local testing
    if 'OUTPUT_PATH' in os.environ:
        fptr = open(os.environ['OUTPUT_PATH'], 'w')
    else:
        fptr = None

    t = int(input().strip())

    for _ in range(t):
        a = input().strip()
        b = input().strip()

        result = buildPalindrome(a, b)

        if fptr:
            fptr.write(result + '\n')
        else:
            print(result)

    if fptr:
        fptr.close()
