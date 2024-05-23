#!/usr/bin/python3
"""
UTF-8 Validation Module
"""


def validUTF8(data):
    """
    Checks if a list of integers represents a valid UTF-8 encoding.
    """
    byte_count = 0
    for byte in data:
        if type(byte) != int or byte < 0 or byte > 0x10ffff:
            return False

        if not (0 <= byte <= 0x10ffff):
            return False
        if byte >> 7 == 0:
            byte_count = 0
        elif byte >> 5 == 0b110:
            byte_count = 1
        elif byte >> 4 == 0b1110:
            byte_count = 2
        elif byte >> 3 == 0b11110:
            byte_count = 3
        else:
            return False
        for _ in range(byte_count):
            if data[1 + byte_count - _] >> 6 != 0b10:
                return False
        byte_count = 0
    return True
