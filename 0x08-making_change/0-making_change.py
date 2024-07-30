#!/usr/bin/python3

def makeChange(coins, total):
    """
    Calculate the minimum number of coins to meet the total change
        
    Args:
        coins (list of integers): Available coins values
        total (int): The total change amount to be returned
    
    Returns: The minimum number of coins to meet the total
        Or 0 if total eqauls 0
        Or -1 if total can't be by any number of coins
    """
    if total == 0:
        return 0
    if total < 0:
        return -1
    
    coins.sort(reverse=True)
    
    min_coins = 0
    n = len(coins) - 1
    for coin in coins:
        while total >= coin:
            total -= coin
            min_coins += 1

    if total == 0:
        return min_coins
    else:
        return -1