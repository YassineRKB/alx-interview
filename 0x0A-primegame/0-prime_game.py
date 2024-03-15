#!/usr/bin/python3
"""Module to determine the winner of a prime game session"""


def isWinner(x, nums):
    """Determine the winner of a prime game session"""
    if x < 1 or not nums:
        return None
    max_num = max(nums)
    primes = [True] * (max_num + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(max_num**0.5) + 1):
        if primes[i]:
            for j in range(i*i, max_num + 1, i):
                primes[j] = False
    mariaw, benw = 0, 0
    for nless in nums:
        primes_count = sum(1 for prime in primes[:nless + 1] if prime)
        if primes_count % 2 == 1:
            mariaw += 1
        else:
            benw += 1
    if mariaw == benw:
        return None
    elif mariaw > benw:
        return 'Maria'
    else:
        return 'Ben'
