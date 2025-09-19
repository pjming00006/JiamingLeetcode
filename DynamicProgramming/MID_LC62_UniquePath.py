"""
There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.



Example 1:


Input: m = 3, n = 7
Output: 28
Example 2:

Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down


Constraints:

1 <= m, n <= 100
"""


class Solution:
    def uniquePathsBacktrack(self, m: int, n: int) -> int:
        """
        Works, but exceed time limit because call stack becomes too deep
        """
        res = 0

        def backtrack(M, N):
            nonlocal m, n, res
            if M == m and N == n:
                res += 1
                return

            # Try move right if possible
            if N < n:
                backtrack(M, N + 1)
            # Try move down if possible
            if M < m:
                backtrack(M + 1, N)

            return

        backtrack(1, 1)
        return res

    def uniquePathsDPIteration(self, m: int, n: int) -> int:
        memo = [[0 for i in range(n)] for j in range(m)]
        # To get to each cell of first row, there is always 1 way
        for i in range(n):
            memo[0][i] = 1
        # To get to each cell of first column, there is always 1 way
        for j in range(m):
            memo[j][0] = 1

        for M in range(1, m):
            for N in range(1, n):
                memo[M][N] = memo[M - 1][N] + memo[M][N - 1]

        return memo[-1][-1]






