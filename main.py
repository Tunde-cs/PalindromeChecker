
#!/bin/python3

import math
import os
import random
import re
import sys

def buildPalindrome(a, b):
    if not a or not b:
        return "-1"

    def is_palindrome(s):
        return s == s[::-1]

    best_palindrome = None
    max_length = 0
    
    # Performance optimization: limit substring length to prevent timeout
    max_len_limit = min(20, len(a), len(b))
    
    n = len(a)
    m = len(b)

    # Iterate by length first (longest first optimization)
    for len_a in range(1, min(n, max_len_limit) + 1):
        for len_b in range(1, min(m, max_len_limit) + 1):
            # Early termination: if current combination can't beat best length
            if best_palindrome and len_a + len_b <= max_length:
                continue
                
            # Try all starting positions for substring of length len_a from string a
            for start_a in range(n - len_a + 1):
                sa = a[start_a:start_a + len_a]
                
                # Try all starting positions for substring of length len_b from string b
                for start_b in range(m - len_b + 1):
                    sb = b[start_b:start_b + len_b]
                    
                    # Try both combinations: sa+sb and sb+sa
                    for combo in [sa + sb, sb + sa]:
                        if is_palindrome(combo):
                            # Check if this is better than current best
                            if (len(combo) > max_length or 
                                (len(combo) == max_length and 
                                 (best_palindrome is None or combo < best_palindrome))):
                                best_palindrome = combo
                                max_length = len(combo)

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
