#!/usr/bin/python3
"""coin change problem"""


def make_change(coins, total):
    """Return the fewest number of coins needed to make up the total"""
    if total <= 0:
        return 0
    coins.sort(reverse=True)
    count = 0
    for coin in coins:
        count += total // coin
        total %= coin
    return count if total == 0 else -1
