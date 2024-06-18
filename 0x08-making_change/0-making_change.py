#!/usr/bin/python3

def makeChange(coins, total):
    if total <= 0:
        return 0

    # Initialize dp array with a large value representing infinity
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: 0 coins needed to make the amount 0

    # Update the dp array
    for i in range(1, total + 1):
        for coin in coins:
            if i >= coin:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    # If dp[total] is still infinity, it means it's not possible to make that amount
    return dp[total] if dp[total] != float('inf') else -1

# Example usage:
if __name__ == "__main__":
    print(makeChange([1, 2, 25], 37))  # Output: 7
    print(makeChange([1256, 54, 48, 16, 102], 1453))  # Output: -1
