#!/usr/bin/python3
"""This module contains the function for the minimum operations problem."""


def minOperations(n: int) -> int:
    """
    Function to calculate minimum operations required to reach n'H' characters
    in a file containing a single 'H' character using the two allowed
    operations `Copy_All` and `Paste`

    Args:
        n (int): The targeted character count

    Returns:
        The Count of operations needed to reach the character count n
    """

    OpCount, factor = 0, 2

    while factor * factor <= n:
        if n % factor:
            factor += 1
        else:
            n //= factor
            OpCount += factor

    if n > 1:
        OpCount += n

    return OpCount
