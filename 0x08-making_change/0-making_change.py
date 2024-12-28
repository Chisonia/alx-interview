#!/usr/bin/python3
'''Coin change module'''


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given total.

    Args:
        coins (list): List of coin denominations.
        total (int): The total amount to achieve.

    Returns:
        int: Fewest number of coins needed or -1 if total cannot be met.
    """
    if total <= 0:
        return 0

    # Initialize the DP table
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: 0 coins needed to make total 0

    # Fill the DP table
    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    # Return the result
    return dp[total] if dp[total] != float('inf') else -1
