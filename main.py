
#!/bin/python3

import math
import os
import random
import re
import sys

def buildPalindrome(a, b):
    print(f"DEBUG: Input a='{a}', b='{b}'")
    
    if not a or not b:
        print("DEBUG: One or both strings are empty")
        return "-1"

    best_palindrome = None
    best_length = 0
    palindromes_found = []

    print(f"DEBUG: Starting substring combination search...")
    
    # Try all possible substring combinations
    for len_a in range(1, len(a) + 1):
        for start_a in range(len(a) - len_a + 1):
            sa = a[start_a:start_a + len_a]

            for len_b in range(1, len(b) + 1):
                for start_b in range(len(b) - len_b + 1):
                    sb = b[start_b:start_b + len_b]

                    # Try both combinations: sa+sb and sb+sa
                    for combo in [sa + sb, sb + sa]:
                        print(f"DEBUG: Trying combo '{combo}' (sa='{sa}', sb='{sb}')")
                        
                        if combo == combo[::-1]:  # is palindrome
                            combo_len = len(combo)
                            palindromes_found.append(combo)
                            print(f"DEBUG: Found palindrome '{combo}' with length {combo_len}")

                            # Update best if this is longer, or same length but lexicographically smaller
                            if (combo_len > best_length or 
                                (combo_len == best_length and (best_palindrome is None or combo < best_palindrome))):
                                print(f"DEBUG: New best palindrome: '{combo}' (prev: '{best_palindrome}')")
                                best_palindrome = combo
                                best_length = combo_len

    print(f"DEBUG: After substring combinations, best='{best_palindrome}', length={best_length}")
    print(f"DEBUG: All palindromes found so far: {palindromes_found}")

    print(f"DEBUG: Starting reversed substring search...")
    
    # Also try combinations with reversed substrings
    for len_a in range(1, len(a) + 1):
        for start_a in range(len(a) - len_a + 1):
            sa = a[start_a:start_a + len_a]
            sa_rev = sa[::-1]

            for len_b in range(1, len(b) + 1):
                for start_b in range(len(b) - len_b + 1):
                    sb = b[start_b:start_b + len_b]
                    sb_rev = sb[::-1]

                    # Try combinations with reverses: sa+sb_rev, sa_rev+sb, etc.
                    for combo in [sa + sb_rev, sa_rev + sb, sb + sa_rev, sb_rev + sa]:
                        print(f"DEBUG: Trying reversed combo '{combo}' (sa='{sa}', sa_rev='{sa_rev}', sb='{sb}', sb_rev='{sb_rev}')")
                        
                        if combo == combo[::-1]:  # is palindrome
                            combo_len = len(combo)
                            palindromes_found.append(combo)
                            print(f"DEBUG: Found palindrome '{combo}' with length {combo_len}")

                            # Update best if this is longer, or same length but lexicographically smaller
                            if (combo_len > best_length or 
                                (combo_len == best_length and (best_palindrome is None or combo < best_palindrome))):
                                print(f"DEBUG: New best palindrome: '{combo}' (prev: '{best_palindrome}')")
                                best_palindrome = combo
                                best_length = combo_len

    print(f"DEBUG: Final result: '{best_palindrome}' with length {best_length}")
    print(f"DEBUG: All palindromes found: {sorted(set(palindromes_found))}")
    
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
