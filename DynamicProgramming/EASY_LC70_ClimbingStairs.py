"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?



Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step


Constraints:

1 <= n <= 45
"""

class Solution:
    def climbStairsDP(self, n: int) -> int:
        """
        Idea: to get to the nth stair, how many ways are there?

        nth stair can be achieved by either adding 1 step from n-1 or adding 2 step from n-2
        So the number of ways at n is the sum of number of ways at n-1 and n-2.

        *Why doesn't count the +1 and the +2 step? Because they don't increase the number of ways to get to n

        Time, Space: O(n)
        """
        if n == 1:
            return 1
        elif n == 2:
            return 2

        dp = [0 for _ in range(n)]
        dp[0], dp[1] = 1, 2
        for i in range(2, n):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n - 1]

    def climbStairsFibonacci(self, n: int) -> int:
        """
        Time: O(n), Space: O(1)
        """
        if n == 1:
            return 1
        elif n == 2:
            return 2

        first = 1
        second = 2
        for i in range(3, n + 1):
            third = first + second
            first = second
            second = third
        return third