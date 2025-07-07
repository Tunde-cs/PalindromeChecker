def is_palindrome(s):
    return s == s[::-1]

def buildPalindrome(a, b):
    # Early exit for empty strings
    if not a or not b:
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

    # Try all combinations: both sa + sb and sb + sa
    for sa in substrings_a:
        for sb in substrings_b:
            # Try both orders of concatenation
            for candidate in [sa + sb, sb + sa]:
                if is_palindrome(candidate):
                    # Update best if this candidate is better
                    # Priority: longest first, then lexicographically smallest
                    if (best is None or 
                        len(candidate) > len(best) or 
                        (len(candidate) == len(best) and candidate < best)):
                        best = candidate

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