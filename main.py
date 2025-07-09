
#!/bin/python3

import os

def is_palindrome(s):
    """Check if a string is a palindrome."""
    return s == s[::-1]

def find_all_palindromes(a, b, max_limit=60, debug=False):
    """Find all possible palindromes and return them sorted by length and lexicographically."""
    if not a or not b:
        return []

    palindromes = []
    
    if debug:
        print(f"DEBUG: Starting search with a='{a[:20]}...' (len={len(a)}), b='{b[:20]}...' (len={len(b)})")
        print(f"DEBUG: Max limit = {max_limit}")
    
    palindrome_count = 0
    
    # Try all combinations of substrings from a and b
    for len_a in range(1, min(len(a), max_limit) + 1):
        for start_a in range(len(a) - len_a + 1):
            sa = a[start_a:start_a + len_a]
            
            for len_b in range(1, min(len(b), max_limit) + 1):
                for start_b in range(len(b) - len_b + 1):
                    sb = b[start_b:start_b + len_b]
                    
                    # Try both concatenation orders
                    for candidate in [sa + sb, sb + sa]:
                        if is_palindrome(candidate):
                            palindrome_count += 1
                            palindromes.append(candidate)
                            
                            if debug and palindrome_count <= 10:
                                print(f"DEBUG: Found palindrome #{palindrome_count}: '{candidate}' (len={len(candidate)}) from '{sa}' + '{sb}'")
    
    # Remove duplicates and sort
    unique_palindromes = list(set(palindromes))
    
    if debug:
        print(f"DEBUG: Total palindromes found: {len(palindromes)}, unique: {len(unique_palindromes)}")
        if unique_palindromes:
            print(f"DEBUG: Longest palindrome length: {len(max(unique_palindromes, key=len))}")
    
    # Sort by length (descending), then lexicographically (descending for largest)
    unique_palindromes.sort(key=lambda x: (-len(x), -ord(x[0]) if x else 0), reverse=False)
    
    return unique_palindromes

def buildPalindrome(a, b, debug=False):
    """
    Build the longest palindrome from substrings of a and b.
    If there are ties in length, return the lexicographically largest.
    """
    palindromes = find_all_palindromes(a, b, debug=debug)
    
    if not palindromes:
        if debug:
            print(f"DEBUG: No palindromes found, returning -1")
        return "-1"
    
    # Find the maximum length
    max_length = len(palindromes[0])
    
    # Get all palindromes with maximum length
    max_palindromes = [p for p in palindromes if len(p) == max_length]
    
    if debug:
        print(f"DEBUG: Found {len(max_palindromes)} palindromes with max length {max_length}")
        print(f"DEBUG: Max length palindromes: {max_palindromes[:5]}")  # Show first 5
        print(f"DEBUG: Lexicographically largest: '{max(max_palindromes)}'")
    
    # Return the lexicographically largest among the longest
    return max(max_palindromes)

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
