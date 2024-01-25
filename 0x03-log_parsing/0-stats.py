#!/usr/bin/python3
"""Script to read stdin line by line"""
from sys import stdin


statusCodes = {"200": 0, "301": 0, "400": 0, "401": 0,
               "403": 0, "404": 0, "405": 0, "500": 0}
size = 0
counter = 0


def print_stats(status_codes, file_size):
    """Prints stats"""
    print("File size: {}".format(file_size))
    for key, value in sorted(status_codes.items()):
        print("{}: {}".format(key, value)) if value != 0 else None


if __name__ == "__main__":
    try:
        for line in stdin:
            data = line.split()
            counter += 1
            try:
                size += int(data[-1])
                statusCodes[data[-2]] += 1
            except Exception:
                pass
            print_stats(statusCodes, size) if counter % 10 == 0 else None
        print_stats(statusCodes, size)
    except KeyboardInterrupt:
        print_stats(statusCodes, size)
        raise
