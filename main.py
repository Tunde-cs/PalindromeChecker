
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
    for i in range(len(a)):
        for j in range(i + 1, len(a) + 1):
            sa = a[i:j]
            
            for k in range(len(b)):
                for l in range(k + 1, len(b) + 1):
                    sb = b[k:l]
                    
                    # Try both combinations: sa + sb and sb + sa
                    for combo in [sa + sb, sb + sa]:
                        if is_palindrome(combo):
                            combo_len = len(combo)
                            
                            # Update if longer, or same length but lexicographically smaller
                            if (combo_len > best_length or 
                                (combo_len == best_length and (best_palindrome is None or combo < best_palindrome))):
                                best_palindrome = combo
                                best_length = combo_len
    
    return best_palindrome if best_palindrome else "-1"


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        a = input().strip()
        b = input().strip()
        print(buildPalindrome(a, b))
