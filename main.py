def is_palindrome(s):
    return s == s[::-1]

def buildPalindrome(a, b):
    best = None

    def is_palindrome(s):
        return s == s[::-1]

    # Early exit for empty strings
    if not a or not b:
        return "-1"

    n = len(a)
    m = len(b)

    for i in range(n):
        for j in range(i + 1, n + 1):
            sa = a[i:j]
            for k in range(m):
                for l in range(k + 1, m + 1):
                    sb = b[k:l]

                    # Try both sa + sb and sb + sa (without reversing)
                    for combo in [sa + sb, sb + sa]:
                        if is_palindrome(combo):
                            # Priority: longest first, then lexicographically smallest
                            if (best is None or 
                                len(combo) > len(best) or 
                                (len(combo) == len(best) and combo < best)):
                                best = combo

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