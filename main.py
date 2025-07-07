
def is_palindrome(s):
    return s == s[::-1]

def buildPalindrome(a, b):
    best = None
    max_len = 0
    
    # Much more aggressive length limit for efficiency
    max_len_limit = min(20, len(a), len(b))
    
    # Try smaller substrings first, focusing on likely palindrome patterns
    for len_a in range(1, min(len(a) + 1, max_len_limit + 1)):
        for start_a in range(len(a) - len_a + 1):
            sa = a[start_a:start_a + len_a]
            
            for len_b in range(1, min(len(b) + 1, max_len_limit + 1)):
                for start_b in range(len(b) - len_b + 1):
                    sb = b[start_b:start_b + len_b]
                    
                    # Test both combinations
                    for cand in [sa + sb, sb + sa]:
                        if len(cand) <= max_len_limit * 2 and is_palindrome(cand):
                            if len(cand) > max_len or (len(cand) == max_len and (best is None or cand < best)):
                                max_len = len(cand)
                                best = cand
    
    return best if best else "-1"

# Read input
n = int(input())
for _ in range(n):
    a = input().strip()
    b = input().strip()
    result = buildPalindrome(a, b)
    print(result)
