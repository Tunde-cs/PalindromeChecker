
def is_palindrome(s):
    return s == s[::-1]

def buildPalindrome(a, b):
    print(f"DEBUG: Processing a='{a}', b='{b}'")
    
    # Early exit for empty strings
    if not a or not b:
        print("DEBUG: Empty string detected, returning -1")
        return "-1"
    
    # Check if there are any common characters
    common_chars = set(a) & set(b)
    if not common_chars:
        print("DEBUG: No common characters, returning -1")
        return "-1"
    
    print(f"DEBUG: Common characters: {common_chars}")
    
    best = None
    max_len = 0
    
    # Try all possible substrings from both strings
    print("DEBUG: Trying substring combinations...")
    
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
    
    print(f"DEBUG: Found {len(substrings_a)} substrings from a, {len(substrings_b)} from b")
    print(f"DEBUG: Sample substrings from a: {substrings_a[:10]}")
    print(f"DEBUG: Sample substrings from b: {substrings_b[:10]}")
    
    palindromes_found = []
    
    # Try all combinations: sa + sb and sb + sa
    for sa in substrings_a:
        for sb in substrings_b:
            for cand in [sa + sb, sb + sa]:
                if is_palindrome(cand):
                    palindromes_found.append(cand)
                    # Prioritize: longest first, then lexicographically smallest
                    if (best is None or 
                        len(cand) > len(best) or 
                        (len(cand) == len(best) and cand < best)):
                        print(f"DEBUG: New best substring candidate: '{cand}'")
                        best = cand
    
    print(f"DEBUG: Total palindromes found: {len(palindromes_found)}")
    if len(palindromes_found) <= 20:  # Only show if not too many
        print(f"DEBUG: All palindromes: {sorted(set(palindromes_found))}")
    print(f"DEBUG: Final best result: '{best}'")
    
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
