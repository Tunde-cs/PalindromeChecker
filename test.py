from main import buildPalindrome

test_cases = [
    ("bac", "bac"),       # expect "aba"
    ("abc", "def"),       # expect "-1"
    ("jdfh", "fds"),      # expect "dfhfd"
    ("abc", "cba"),       # "abcba"
    ("", ""),             # both empty
    ("a", ""),            # one empty
    ("aa", "aa"),         # expect "aaaa"
    ("race", "car"),      # expect "racecar"
]

for a, b in test_cases:
    result = buildPalindrome(a, b)
    print(f"Result for a='{a}', b='{b}': {result}")
