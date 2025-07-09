
#!/bin/python3

import os
from collections import Counter

def buildPalindrome(a, b):
    """Build palindrome using optimal character arrangement from both strings."""
    if not a or not b:
        return "-1"
    
    # Get all available characters
    all_chars = Counter(a + b)
    
    # Build the longest possible palindrome
    left_half = []
    middle_char = ""
    
    # Sort characters to ensure lexicographic order
    for char in sorted(all_chars.keys()):
        count = all_chars[char]
        # Use pairs for the sides
        pairs = count // 2
        left_half.extend([char] * pairs)
        
        # Keep track of the lexicographically smallest odd-count character for middle
        if count % 2 == 1 and middle_char == "":
            middle_char = char
    
    # Build palindrome: left + middle + right
    if not left_half and not middle_char:
        return "-1"
    
    left_str = ''.join(left_half)
    right_str = left_str[::-1]
    result = left_str + middle_char + right_str
    
    return result if result else "-1"

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
