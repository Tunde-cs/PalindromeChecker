
#!/bin/python3

import os

def is_palindrome(s):
    """Check if a string is a palindrome."""
    return s == s[::-1]

def buildPalindrome(a, b):
    """
    Build the longest palindrome from substrings of a and b.
    For ties in length, return the lexicographically smallest palindrome.
    """
    if not a or not b:
        return "-1"

    best_palindrome = None
    max_length = 0
    
    # Optimization: limit substring length to avoid timeout
    max_len_a = min(len(a), 20)
    max_len_b = min(len(b), 20)

    # Try all combinations of substrings from a and b
    for len_a in range(1, max_len_a + 1):
        for start_a in range(len(a) - len_a + 1):
            sa = a[start_a:start_a + len_a]
            
            for len_b in range(1, max_len_b + 1):
                for start_b in range(len(b) - len_b + 1):
                    sb = b[start_b:start_b + len_b]
                    
                    # Try both concatenation orders
                    for candidate in [sa + sb, sb + sa]:
                        if is_palindrome(candidate):
                            candidate_length = len(candidate)

                            # Check if this is better than current best
                            if (candidate_length > max_length or 
                                (candidate_length == max_length and 
                                 (best_palindrome is None or candidate > best_palindrome))):
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
