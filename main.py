#!/bin/python3
import math
import os
import random
import re
import sys
from collections import Counter


def buildPalindrome(a, b):
    print(f"\n[DEBUG] Input a: '{a}', b: '{b}'")

    if not a or not b:
        print("[DEBUG] One of the strings is empty. Returning '-1'.")
        return "-1"

    count_a = Counter(a)
    count_b = Counter(b)
    print(f"[DEBUG] Counter a: {count_a}, Counter b: {count_b}")

    common_chars = set(count_a.keys()) & set(count_b.keys())
    print(f"[DEBUG] Common chars: {common_chars}")

    if not common_chars:
        print("[DEBUG] No common chars. Returning '-1'.")
        return "-1"

    best = None

    def try_palindrome(s):
        nonlocal best
        if s and (best is None or len(s) > len(best) or
                  (len(s) == len(best) and s < best)):

            print(
                f"[DEBUG] New best palindrome found: '{s}' (old best: '{best}')"
            )
            best = s

    def get_subsequences(s):
        subsequences = []
        n = len(s)
        for i in range(1, 1 << n):
            subseq = ""
            for j in range(n):
                if i & (1 << j):
                    subseq += s[j]
            subsequences.append(subseq)
        return subsequences

    subs_a = get_subsequences(a)
    subs_b = get_subsequences(b)
    print(f"[DEBUG] Generated {len(subs_a)} subsequences for '{a}'")
    print(f"[DEBUG] Generated {len(subs_b)} subsequences for '{b}'")

    for sa in subs_a:
        for sb in subs_b:
            for combo in [sa + sb, sb + sa]:
                if combo == combo[::-1]:
                    try_palindrome(combo)

    print(f"[DEBUG] Returning: '{best if best else '-1'}'")
    return best if best else "-1"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input().strip())
    for test_num in range(t):
        a = input().strip()
        b = input().strip()
        result = buildPalindrome(a, b)
        print(f"[DEBUG] Test case {test_num+1} result: {result}"
              )  # Debug test case result
        fptr.write(result + '\n')
    fptr.close()
