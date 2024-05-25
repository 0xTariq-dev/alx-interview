#!/usr/bin/python3
"""
UTF-8 Validation Module
"""


def validUTF8(data):
    """
    Checks if a list of integers represents a valid UTF-8 encoding.
    """
    byte_count = 0
    for i in range(len(data)):
        byte = data[i]

        if type(byte) != int or byte < 0 or byte > 255:
            return False

        if byte_count == 0:
            if byte >> 7 == 0:
                continue
            elif byte >> 5 == 0b110:
                byte_count = 1
            elif byte >> 4 == 0b1110:
                byte_count = 2
            elif byte >> 3 == 0b11110:
                byte_count = 3
            else:
                return False
        else:
            if byte >> 6 != 0b10:
                return False
            byte_count -= 1
    return byte_count == 0
