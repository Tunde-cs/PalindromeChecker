
def is_palindrome(s):
    return s == s[::-1]

def get_all_substrings(s):
    substrings = []
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            substrings.append(s[i:j])
    return substrings

# Test case: a='bac', b='bac'
a = 'bac'
b = 'bac'

print(f"String a='{a}' substrings: {get_all_substrings(a)}")
print(f"String b='{b}' substrings: {get_all_substrings(b)}")

palindromes = []
for sa in get_all_substrings(a):
    for sb in get_all_substrings(b):
        for candidate in [sa + sb, sb + sa]:
            if is_palindrome(candidate):
                palindromes.append((candidate, len(candidate), sa, sb))

palindromes.sort(key=lambda x: (-x[1], x[0]))
print(f"\nAll possible palindromes (sorted by length desc, then lexicographically):")
for p, length, sa, sb in palindromes:
    print(f"'{p}' (length {length}) from '{sa}' + '{sb}'")

print(f"\nLongest palindrome: '{palindromes[0][0]}' (length {palindromes[0][1]})")

# Check if 'baccab' is actually a palindrome
test = 'baccab'
print(f"\nIs '{test}' a palindrome? {is_palindrome(test)}")
print(f"'{test}' reversed: '{test[::-1]}'")
