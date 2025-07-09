
#!/bin/python3

import os

def is_palindrome(s):
    """Check if a string is a palindrome."""
    return s == s[::-1]

def find_all_palindromes(a, b, max_limit=50):
    """Find all possible palindromes and return them sorted by length and lexicographically."""
    if not a or not b:
        return []

    palindromes = []
    
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
                            palindromes.append(candidate)
    
    # Remove duplicates and sort
    unique_palindromes = list(set(palindromes))
    # Sort by length (descending), then lexicographically (ascending)
    unique_palindromes.sort(key=lambda x: (-len(x), x))
    
    return unique_palindromes

def buildPalindrome(a, b):
    """
    Build the longest palindrome from substrings of a and b.
    If there are ties in length, return the lexicographically smallest.
    """
    palindromes = find_all_palindromes(a, b)
    
    if not palindromes:
        return "-1"
    
    # Find the maximum length
    max_length = len(palindromes[0])
    
    # Get all palindromes with maximum length
    max_palindromes = [p for p in palindromes if len(p) == max_length]
    
    # Return the lexicographically smallest among the longest
    return min(max_palindromes)

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
