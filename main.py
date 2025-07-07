#!/bin/python3

import math
import os
import random
import re
import sys


def buildPalindrome(a, b):
    n, m = len(a), len(b)
    best = None
    max_len = 0

    def is_palindrome(s):
        return s == s[::-1]

    max_sub_len = 60  # Adjusted for deep palindromes

    for i in range(n):
        for j in range(i + 1, min(n + 1, i + max_sub_len + 1)):
            sa = a[i:j]
            for k in range(m):
                for l in range(k + 1, min(m + 1, k + max_sub_len + 1)):
                    sb = b[k:l]
                    for combo in [sa + sb, sb + sa]:
                        if is_palindrome(combo):
                            if len(combo) > max_len or (
                                    len(combo) == max_len and
                                (best is None or combo < best)):
                                best = combo
                                max_len = len(combo)

    return best if best else "-1"


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        a = input().strip()
        b = input().strip()
        print(buildPalindrome(a, b))
