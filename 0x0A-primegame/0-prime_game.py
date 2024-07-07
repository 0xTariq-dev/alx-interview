#!/usr/bin/python3
"""Prime Game Challenge Module
"""


def isWinner(x: int, nums: list) -> str:
    """Determins the winner of the game

    Args:
        x (int): The number of rounds in the game
        nums (list): list contain the upper bound for integers
                for each round.

    Returns: The name of the winner
    """
    if x < 1 or not nums:
        return None

    SCORE = {'Maria': 0, 'Ben': 0}
    n = max(nums)
    PRIMES = [True] * (n + 1)
    PRIMES[0] = PRIMES[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if PRIMES[i]:
            for j in range(i * i, n + 1, i):
                PRIMES[j] = False

    primes_count = [0] * (n + 1)
    for i in range(1, n + 1):
        primes_count[i] = primes_count[i - 1] + (1 if PRIMES[i] else 0)

    PLAYER = 'Maria'
    for num in nums:
        count = primes_count[num]
        if count % 2 == 0:
            SCORE['Ben'] += 1
        else:
            SCORE['Maria'] += 1
    PLAYER = max(
        SCORE, key=SCORE.get
        ) if SCORE['Maria'] != SCORE['Ben'] else None
    return PLAYER
