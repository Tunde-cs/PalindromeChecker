from main import buildPalindrome

test_cases = [
    ("bac", "bac"),       # Expected: 'aba'
    ("abc", "def"),       # Expected: '-1'
    ("jdfh", "fds"),      # Expected: 'dfhfd'
    ("abc", "cba"),       # Expected: 'abccba'
    ("", ""),             # Expected: '-1'
    ("a", ""),            # Expected: '-1'
    ("aa", "aa"),         # Expected: 'aaaa'
    ("race", "car"),      # Expected: 'racecar'
]

for a, b in test_cases:
    result = buildPalindrome(a, b)
    print(f"Result for a='{a}', b='{b}': {result}")
