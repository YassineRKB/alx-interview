#!/usr/bin/python3
"""module for Minimum Operations"""


def minOperations(n):
    """calculates the fewest number of
    operations needed to result in exactly
    n H characters in the file."""
    if n > 1:
        i = 2
        count = 0
        while i <= n:
            if n % i != 0:
                i += 1
            else:
                count += i
                n = n / i
        return count
    return 0
