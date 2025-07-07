
def is_palindrome(s):
    return s == s[::-1]

def buildPalindrome(a, b):
    palindromes = []
    
    # Find all possible palindromes
    for len_a in range(1, len(a) + 1):
        for start_a in range(len(a) - len_a + 1):
            sa = a[start_a:start_a + len_a]

            for len_b in range(1, len(b) + 1):
                for start_b in range(len(b) - len_b + 1):
                    sb = b[start_b:start_b + len_b]

                    for cand in [sa + sb, sb + sa]:
                        if is_palindrome(cand):
                            palindromes.append(cand)
    
    if not palindromes:
        return "-1"
    
    # Return the lexicographically smallest palindrome
    return min(palindromes)
