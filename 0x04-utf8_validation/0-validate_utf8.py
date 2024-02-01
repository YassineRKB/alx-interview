#!/usr/bin/python3
"""module for utf8 validation"""


def validUTF8(data):
    """Checks if a list of integers are valid UTF-8 codepoints."""
    n = len(data)
    bCount = 0
    for i in range(n):
        if bCount > 0:
            bCount -= 1
            continue
        if data[i] <= 0x7F:
            bCount = 0
        elif data[i] & 0b11111000 == 0b11110000:
            step = 4
            if n - i >= step:
                next_body = all((data[j] & 0b11000000 == 0b10000000) for j in range(i + 1, i + step))
                if not next_body:
                    return False
                bCount = step - 1
            else:
                return False
        elif data[i] & 0b11110000 == 0b11100000:
            step = 3
            if n - i >= step:
                next_body = all((data[j] & 0b11000000 == 0b10000000) for j in range(i + 1, i + step))
                if not next_body:
                    return False
                bCount = step - 1
            else:
                return False
        elif data[i] & 0b11100000 == 0b11000000:
            step = 2
            if n - i >= step:
                next_body = all((data[j] & 0b11000000 == 0b10000000) for j in range(i + 1, i + step))
                if not next_body:
                    return False
                bCount = step - 1
            else:
                return False
        else:
            return False
    return True

