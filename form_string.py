def form_the_string(n, substrings, main_string):
    # Initialize dp array with a large value (INF) to represent impossible states
    m = len(main_string)
    INF = float('inf')
    dp = [INF] * (m + 1)
    dp[0] = 0  # Base case: cost to form an empty prefix is 0

    # Dynamic programming to calculate the minimum cost
    for i in range(1, m + 1):
        for sub, cost in substrings:
            sub_len = len(sub)
            if i >= sub_len and main_string[i - sub_len:i] == sub:
                dp[i] = min(dp[i], dp[i - sub_len] + cost)

    # Return the result
    return dp[m] if dp[m] != INF else "Impossible"

# Input
n = int(input())  # Number of substrings
substrings = []
for _ in range(n):
    s, c = input().split()
    substrings.append((s, int(c)))  # Store substring and its cost as a tuple
main_string = input()  # The main string

# Solve the problem
result = form_the_string(n, substrings, main_string)
print(result)
