
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

    # Use a set to avoid duplicate palindromes
    palindromes = set()

    # Try all possible substring combinations - exhaustive search
    for len_a in range(1, len(a) + 1):
        for start_a in range(len(a) - len_a + 1):
            sa = a[start_a:start_a + len_a]

            for len_b in range(1, len(b) + 1):
                for start_b in range(len(b) - len_b + 1):
                    sb = b[start_b:start_b + len_b]

                    # Try both concatenation orders
                    for candidate in [sa + sb, sb + sa]:
                        if is_palindrome(candidate):
                            palindromes.add(candidate)
                            
                            if debug and len(candidate) <= 20:
                                print(f"DEBUG: Found palindrome: '{candidate}' (len={len(candidate)}) from '{sa}' + '{sb}'")

    if not palindromes:
        return "-1"

    # Convert to list and sort by length (descending) then lexicographically (ascending)
    palindromes = list(palindromes)
    palindromes.sort(key=lambda x: (-len(x), x))
    best_palindrome = palindromes[0]

    if debug:
        print(f"DEBUG: All unique palindromes found: {len(palindromes)}")
        print(f"DEBUG: Top 5 candidates: {palindromes[:5]}")
        print(f"DEBUG: Final result: '{best_palindrome}' (length: {len(best_palindrome)})")

    return best_palindrome

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
