def is_palindrome(s):
    return s == s[::-1]

def buildPalindrome(a, b):
    print(f"Processing a='{a}' (len={len(a)}), b='{b}' (len={len(b)})")

    best = None
    max_len = 0
    max_limit = 20  # Adjusted for performance

    total_combinations = 0
    palindrome_count = 0

    for len_a in range(1, min(len(a), max_limit) + 1):
        for start_a in range(len(a) - len_a + 1):
            sa = a[start_a:start_a + len_a]

            for len_b in range(1, min(len(b), max_limit) + 1):
                for start_b in range(len(b) - len_b + 1):
                    sb = b[start_b:start_b + len_b]

                    for cand in [sa + sb, sb + sa]:
                        total_combinations += 1
                        if is_palindrome(cand):
                            palindrome_count += 1
                            if len(cand) > max_len or (len(cand) == max_len and (best is None or cand < best)):
                                print(f"New best palindrome: '{cand}' (from '{sa}' + '{sb}')")
                                best = cand
                                max_len = len(cand)

    print(f"Total combinations tested: {total_combinations}")
    print(f"Palindromes found: {palindrome_count}")
    print(f"Best result: {best if best else '-1'}")
    print("----------")

    return best if best else "-1"
