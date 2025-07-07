
def is_palindrome(s):
    return s == s[::-1]

def buildPalindrome(a, b):
    best = None
    max_len = 0
    
    # Limit substring length to prevent exponential growth
    max_sub_len = min(50, len(a), len(b))
    
    # Generate substrings more efficiently
    subs_a = set()
    for i in range(len(a)):
        for j in range(i+1, min(len(a)+1, i+max_sub_len+1)):
            subs_a.add(a[i:j])
    
    subs_b = set()
    for i in range(len(b)):
        for j in range(i+1, min(len(b)+1, i+max_sub_len+1)):
            subs_b.add(b[i:j])
    
    # Test combinations
    for sa in subs_a:
        for sb in subs_b:
            for cand in [sa + sb, sb + sa]:
                if is_palindrome(cand):
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
