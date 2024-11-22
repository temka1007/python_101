def climb_stairs(n, memo=None):
    if memo is None:
        memo = {}

    if n in memo:
        return memo[n]
    elif n == 1:
        return 1
    elif n == 2:
        return 2

    memo[n] = climb_stairs(n - 1, memo) + climb_stairs(n - 2, memo)
    return memo[n]


# Test Cases
print(f"n=2: {climb_stairs(2)}")  # Expected: 2
print(f"n=3: {climb_stairs(3)}")  # Expected: 3
print(f"n=5: {climb_stairs(5)}")  # Expected: 8
print(f"n=10: {climb_stairs(10)}")  # Expected: 89
