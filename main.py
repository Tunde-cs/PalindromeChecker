def is_palindrome(word):
    """Check if a word is a palindrome."""
    reversed_word = word[::-1]
    return word == reversed_word


def all_substrings_of_word(word):
    """Generate all possible non-empty substrings of a given string."""
    substrings = []
    for sub_string_length in range(1, len(word) + 1):
        for i in range(len(word) - sub_string_length + 1):
            new_word = word[i:i + sub_string_length]
            substrings.append(new_word)
    return substrings


def buildPalindrome(a, b):
    """Attempt to find the longest palindromic string created by concatenating
    a substring of `a` with a substring of `b`."""
    sub_strings_a = all_substrings_of_word(a)
    sub_strings_b = all_substrings_of_word(b)

    # Generate all possible concatenations of substrings from `a` and `b`
    multiplexed_array = [
        word_a + word_b for word_a in sub_strings_a for word_b in sub_strings_b]

    # Find the best palindrome (longest, then lexicographically smallest)
    best_palindrome = ""
    for word in multiplexed_array:
        if is_palindrome(word):
            if len(word) > len(best_palindrome):
                best_palindrome = word
            elif len(word) == len(best_palindrome) and word < best_palindrome:
                best_palindrome = word

    return best_palindrome if best_palindrome else "-1"

print(buildPalindrome("bac", "bac"))   # EXPECTED OUTPUT -- aba
print(buildPalindrome("abc", "def"))   # EXPECTED OUTPUT -- -1
print(buildPalindrome("jdfh", "fds"))   # EXPECTED OUTPUT -- dfhfd