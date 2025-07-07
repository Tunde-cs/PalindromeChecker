def is_palindrome(s):
    return s == s[::-1]

def buildPalindrome(a, b):
    print(f"DEBUG: Processing a='{a}', b='{b}'")
    
    # Early exit for empty strings
    if not a or not b:
        print("DEBUG: One or both strings empty, returning -1")
        return "-1"

    best = None
    max_len = 0

    # Try all possible substrings from both strings
    # Get all substrings from a
    substrings_a = []
    for i in range(len(a)):
        for j in range(i + 1, len(a) + 1):
            substrings_a.append(a[i:j])

    # Get all substrings from b
    substrings_b = []
    for i in range(len(b)):
        for j in range(i + 1, len(b) + 1):
            substrings_b.append(b[i:j])

    print(f"DEBUG: Found {len(substrings_a)} substrings from a: {substrings_a}")
    print(f"DEBUG: Found {len(substrings_b)} substrings from b: {substrings_b}")

    palindromes_found = []

    # Try all combinations: both sa + sb and sb + sa
    for sa in substrings_a:
        for sb in substrings_b:
            # Try both orders of concatenation
            for candidate in [sa + sb, sb + sa]:
                if is_palindrome(candidate):
                    palindromes_found.append(candidate)
                    print(f"DEBUG: Found palindrome: '{candidate}' (sa='{sa}', sb='{sb}')")
                    
                    # Update best if this candidate is better
                    # Priority: lexicographically smallest first
                    if (best is None or candidate < best):
                        print(f"DEBUG: New best: '{candidate}' (was '{best}')")
                        best = candidate

    print(f"DEBUG: All palindromes found: {sorted(set(palindromes_found))}")
    print(f"DEBUG: Final best: '{best}'")
    return best if best else "-1"

if __name__ == '__main__':
    import os
    if 'OUTPUT_PATH' in os.environ:
        fptr = open(os.environ['OUTPUT_PATH'], 'w')
        t = int(input().strip())
        for _ in range(t):
            a = input().strip()
            b = input().strip()
            result = buildPalindrome(a, b)
            fptr.write(result + '\n')
        fptr.close()
    else:
        # For local testing
        pass