
def is_palindrome(s):
    return s == s[::-1]

def buildPalindrome(a, b):
    # Early exit for empty strings
    if not a or not b:
        return "-1"
    
    # Check if there are any common characters
    common_chars = set(a) & set(b)
    if not common_chars:
        return "-1"
    
    best = None
    
    # First, try full strings (most important for identical string cases)
    for cand in [a + b, b + a]:
        if is_palindrome(cand):
            if best is None or len(cand) > len(best) or (len(cand) == len(best) and cand < best):
                best = cand
    
    # Generate subsequences efficiently
    def get_subsequences(s, max_len=12):
        subsequences = ['']
        for char in s:
            new_subseqs = []
            for subseq in subsequences:
                if len(subseq) < max_len:
                    new_subseqs.append(subseq + char)
            subsequences.extend(new_subseqs)
        return [s for s in subsequences if s]  # Remove empty string
    
    # Get subsequences from both strings (excluding full strings since we already tried them)
    subseqs_a = [s for s in get_subsequences(a) if s != a]
    subseqs_b = [s for s in get_subsequences(b) if s != b]
    
    # Try all subsequence combinations
    for sa in subseqs_a:
        for sb in subseqs_b:
            for cand in [sa + sb, sb + sa]:
                if is_palindrome(cand):
                    if best is None or len(cand) > len(best) or (len(cand) == len(best) and cand < best):
                        best = cand
    
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
