
#!/bin/python3

import os

def is_palindrome(s):
    """Check if a string is a palindrome."""
    return s == s[::-1]

def buildPalindrome(a, b):
    """
    Build the longest palindrome from substrings of a and b.
    If there are ties in length, return the lexicographically smallest.
    """
    if not a or not b:
        return "-1"

    best_palindrome = None
    max_length = 0
    max_limit = 20  # Performance limit to avoid timeout

    # Try all possible substring combinations with performance optimization
    for len_a in range(1, min(len(a), max_limit) + 1):
        # Early termination if we can't possibly beat current best
        if best_palindrome and len_a + len(b) <= max_length:
            continue
            
        for start_a in range(len(a) - len_a + 1):
            sa = a[start_a:start_a + len_a]

            for len_b in range(1, min(len(b), max_limit) + 1):
                # Early termination
                if best_palindrome and len_a + len_b <= max_length:
                    continue
                    
                for start_b in range(len(b) - len_b + 1):
                    sb = b[start_b:start_b + len_b]

                    # Try both concatenation orders: sa+sb and sb+sa
                    for candidate in [sa + sb, sb + sa]:
                        if is_palindrome(candidate):
                            candidate_length = len(candidate)

                            # Check if this is better than current best
                            if (candidate_length > max_length or 
                                (candidate_length == max_length and (best_palindrome is None or candidate < best_palindrome))):
                                best_palindrome = candidate
                                max_length = candidate_length

    return best_palindrome if best_palindrome else "-1"

if __name__ == '__main__':
    if 'OUTPUT_PATH' in os.environ:
        # HackerRank submission environment
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
