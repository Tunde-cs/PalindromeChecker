
#!/bin/python3

import os

def is_palindrome(s):
    """Check if a string is a palindrome."""
    return s == s[::-1]

def buildPalindrome(a, b, debug=False):
    """
    Build the longest palindrome from substrings of a and b.
    If there are ties in length, return the lexicographically smallest.
    """
    if not a or not b:
        return "-1"

    if debug:
        print(f"DEBUG: Starting search with a='{a[:20]}...' (len={len(a)}), b='{b[:20]}...' (len={len(b)})")

    best_palindrome = None
    max_length = 0

    # Try all possible substring combinations - exhaustive search
    for len_a in range(1, len(a) + 1):
        for start_a in range(len(a) - len_a + 1):
            sa = a[start_a:start_a + len_a]

            for len_b in range(1, len(b) + 1):
                for start_b in range(len(b) - len_b + 1):
                    sb = b[start_b:start_b + len_b]

                    # Try both concatenation orders: sa+sb and sb+sa
                    candidates = [
                        (sa + sb, sa, sb, 'a+b'),
                        (sb + sa, sb, sa, 'b+a')
                    ]
                    
                    for candidate, part1, part2, order in candidates:
                        if is_palindrome(candidate):
                            candidate_length = len(candidate)
                            
                            if debug and candidate_length <= 20:
                                print(f"DEBUG: Found valid palindrome: '{candidate}' (len={candidate_length}) from '{part1}' + '{part2}' ({order})")
                            
                            # Check if this is better than current best
                            if (candidate_length > max_length or 
                                (candidate_length == max_length and (best_palindrome is None or candidate > best_palindrome))):
                                best_palindrome = candidate
                                max_length = candidate_length
                                if debug:
                                    print(f"DEBUG: New best palindrome: '{candidate}' (length {candidate_length})")

    if debug:
        print(f"DEBUG: Final result: '{best_palindrome}' (length: {max_length})")

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
