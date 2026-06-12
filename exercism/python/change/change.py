"""Find the fewest coins needed to make a target value."""


def find_fewest_coins(coins, target):
    """Return the smallest set of coins that sums to target."""
    if target < 0:
        raise ValueError("target can't be negative")

    dp = [None] * (target + 1)
    dp[0] = []

    for amount in range(1, target + 1):
        best = None

        for coin in coins:
            if coin <= amount and dp[amount - coin] is not None:
                candidate = dp[amount - coin] + [coin]

                if best is None or len(candidate) < len(best):
                    best = candidate

        dp[amount] = best

    if dp[target] is None:
        raise ValueError("can't make target with given coins")

    return sorted(dp[target])