#!/bin/python3

import math
import os
import random
import re
import sys


def buildPalindrome(a, b):

    def is_palindrome(s):
        return s == s[::-1]

    best = None

    for len_a in range(1, len(a) + 1):
        for start_a in range(len(a) - len_a + 1):
            sa = a[start_a:start_a + len_a]

            for len_b in range(1, len(b) + 1):
                for start_b in range(len(b) - len_b + 1):
                    sb = b[start_b:start_b + len_b]

                    for combo in [sa + sb, sb + sa]:
                        if is_palindrome(combo):
                            if (best is None or len(combo) > len(best) or
                                (len(combo) == len(best) and combo < best)):
                                best = combo

    return best if best else "-1"


if __name__ == '__main__':
    import os

    if 'OUTPUT_PATH' in os.environ:
        fptr = open(os.environ['OUTPUT_PATH'], 'w')
    else:
        fptr = None

    t = int(input().strip())

    for _ in range(t):
        a = input().strip()
        b = input().strip()
        result = buildPalindrome(a, b)

        if fptr:
            fptr.write(result + '\n')
        else:
            print(result)

    if fptr:
        fptr.close()
