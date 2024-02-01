#!/usr/bin/python3
"""module for utf8 validation"""


def validUTF8(data):
    """method for validating utf8 encoding"""
    bCount = 0
    for byte in data:
        if bCount == 0:
            if byte >> 5 == 0b110:
                bCount = 1
            elif byte >> 4 == 0b1110:
                bCount = 2
            elif byte >> 3 == 0b11110:
                bCount = 3
            elif byte >> 7:
                return False
        else:
            if byte >> 6 != 0b10:
                return False
            bCount -= 1
    return bCount == 0
