# form-the-string
Problem Statement:

Given a set of substrings, each with an associated cost, and a target string, determine the minimum cost to construct the target string by concatenating zero or more of the given substrings.

Formal Definition:

Given:

A set of substrings S = {(s1, c1), (s2, c2), ..., (sn, cn)}, where si is a substring and ci is its associated cost.
A target string T.
Find:

The minimum cost to construct T by concatenating zero or more substrings from S.
Example:

Substrings and costs:

("ab", 2)
("cd", 3)
("abc", 5)
Target string: abcabc

Solution:

Use ("ab", 2) twice and ("cd", 3) once.
Total cost: 2 * 2 + 3 = 7




Approch:
Dynamic Programming Approach

Problem:
The problem is to determine the minimum cost to form a given main_string using a set of substrings and their associated costs. Each substring can be used multiple times.

Solution Approach:
The code employs a dynamic programming (DP) approach to solve this problem efficiently. Here's a breakdown of the steps:

Initialization:

dp array: An array of size m+1 is initialized, where m is the length of the main_string. Each element dp[i] will store the minimum cost to form the prefix of the main_string up to index i-1.
INF: A large value is assigned to INF to represent impossible states, i.e., when a prefix cannot be formed using the given substrings.
Dynamic Programming Loop:

The outer loop iterates over each character of the main_string.
The inner loop iterates over each substring and its cost.
For each substring sub and its cost cost:
If the current prefix of the main_string ends with sub, we consider the possibility of using sub to form this prefix.
We calculate the cost of forming the current prefix using sub as dp[i-sub_len] + cost.
We update dp[i] with the minimum cost, either the previous value or the newly calculated cost.
Return the Result:

If dp[m] is not INF, it means we can form the entire main_string and the value represents the minimum cost.
Otherwise, if dp[m] is INF, it means the main_string cannot be formed using the given substrings.
Time Complexity:
The time complexity of this algorithm is O(m * n), where m is the length of the main_string and n is the number of substrings.

Space Complexity:
The space complexity is O(m) due to the dp array.

Key Points:

The DP approach efficiently avoids redundant calculations by storing intermediate results.
The dp array acts as a memoization table, helping to optimize the solution.
The INF value is used to handle cases where a prefix cannot be formed.
By understanding this code and the underlying DP technique, you can effectively solve similar string formation problems with varying constraints and costs.






