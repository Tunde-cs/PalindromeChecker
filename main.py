

#!/bin/python3

import math
import os
import random
import re
import sys

def buildPalindrome(a, b):
    best = None
    max_len = 0

    # Try all possible substring combinations
    # For performance, limit individual substring length but be more systematic
    max_individual_len = min(100, len(a), len(b))

    for len_a in range(1, min(len(a) + 1, max_individual_len + 1)):
        for start_a in range(len(a) - len_a + 1):
            substr_a = a[start_a:start_a + len_a]

            for len_b in range(1, min(len(b) + 1, max_individual_len + 1)):
                for start_b in range(len(b) - len_b + 1):
                    substr_b = b[start_b:start_b + len_b]

                    # Try both concatenation orders
                    for candidate in [substr_a + substr_b, substr_b + substr_a]:
                        # Check if it's a palindrome
                        if candidate == candidate[::-1]:
                            # Update best if this is better
                            if (len(candidate) > max_len or 
                                (len(candidate) == max_len and (best is None or candidate < best))):
                                best = candidate
                                max_len = len(candidate)

    return best if best else "-1"

if __name__ == '__main__':
    if 'OUTPUT_PATH' in os.environ:
        # Submission environment
        fptr = open(os.environ['OUTPUT_PATH'], 'w')
        t = int(input().strip())

        for _ in range(t):
            a = input().strip()
            b = input().strip()
            result = buildPalindrome(a, b)
            fptr.write(result + '\n')

        fptr.close()
    else:
        # Local testing
        t = int(input().strip())
        
        for _ in range(t):
            a = input().strip()
            b = input().strip()
            result = buildPalindrome(a, b)
            print(result)
