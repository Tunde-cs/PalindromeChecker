def is_palindrome(s):
    return s == s[::-1]

def buildPalindrome(a, b):
    best = None
    max_len = 0
    max_limit = 20  # Safe for performance

    for len_a in range(1, min(len(a), max_limit) + 1):
        for start_a in range(len(a) - len_a + 1):
            sa = a[start_a:start_a + len_a]

            for len_b in range(1, min(len(b), max_limit) + 1):
                for start_b in range(len(b) - len_b + 1):
                    sb = b[start_b:start_b + len_b]

                    for cand in [sa + sb, sb + sa]:
                        if is_palindrome(cand):
                            if len(cand) > max_len or (len(cand) == max_len and (best is None or cand < best)):
                                best = cand
                                max_len = len(cand)

    return best if best else "-1"

# Local test cases
test_cases = [
    ("bac", "bac"),   # ✅ expected: aba
    ("abc", "def"),   # ✅ expected: -1
    ("jdfh", "fds"),  # ✅ expected: dfhfd
]

for a, b in test_cases:
    result = buildPalindrome(a, b)
    print(f"Result for a='{a}', b='{b}':", result)
