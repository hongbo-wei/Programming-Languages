def fibonacci_dp(n):
    """
    This function calculates the nth Fibonacci number using dynamic programming.

    Args:
        n: The index of the Fibonacci number to calculate.

    Returns:
        The nth Fibonacci number.
    """
    # Base cases
    if n == 0:
        return 0
    elif n == 1:
        return 1

    # Create a DP table to store Fibonacci numbers
    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = 1

    # Fill the DP table using bottom-up approach
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]

    print(dp)
    # Return the nth Fibonacci number from the DP table
    return dp[n]

# Example usage
n = 10
result = fibonacci_dp(n)
print(f"The {n}th Fibonacci number is: {result}")
