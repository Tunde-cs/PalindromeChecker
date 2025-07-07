
#!/bin/python3

import math
import os
import random
import re
import sys


def buildPalindrome(a, b):
    def is_palindrome(s):
        return s == s[::-1]

    best_palindrome = None
    best_length = 0
    
    # Try all possible substrings from both strings
    for len_a in range(1, len(a) + 1):
        for start_a in range(len(a) - len_a + 1):
            sa = a[start_a:start_a + len_a]
            sa_rev = sa[::-1]
            
            for len_b in range(1, len(b) + 1):
                for start_b in range(len(b) - len_b + 1):
                    sb = b[start_b:start_b + len_b]
                    sb_rev = sb[::-1]
                    
                    # Try all combinations: normal + normal, normal + reverse, reverse + normal, reverse + reverse
                    for combo in [sa + sb, sb + sa, sa + sb_rev, sb_rev + sa, sa_rev + sb, sb + sa_rev, sa_rev + sb_rev, sb_rev + sa_rev]:
                        if combo == combo[::-1]:  # is palindrome
                            combo_len = len(combo)
                            if (combo_len > best_length or 
                                (combo_len == best_length and (best_palindrome is None or combo < best_palindrome))):
                                best_palindrome = combo
                                best_length = combo_len

    return best_palindrome if best_palindrome else "-1"


if __name__ == '__main__':
    import os

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
