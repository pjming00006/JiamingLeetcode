"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the
ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.



Example 1:


Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case,
the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1


Constraints:

n == height.length
2 <= n <= 105
0 <= height[i] <= 104
"""


class Solution:
    def maxAreaBruteForce(self, height: list[int]) -> int:
        """
        Brute Force:
        - Use a nested for loop to exhaust all combinations, calculate area and update if this is the current max

        Time: O(n^2)
        Space: O(n)
        """
        res = 0

        for i in range(len(height)):
            for j in range(i+1, len(height)):
                area = min(height[i], height[j]) * (j-i)
                res = max(res, area)
        return res

    def maxAreaTwoPointers(self, height: list[int]) -> int:
        """
        Two Pointer

        Observations:
        In the ideal case, when number of heights is n, the biggest area we could get is when the starting and ending
        bars are the highest, because the length is the longest(area = length * min of the 2 heights)

        Time: O(n)
        Space: O(n)
        """
        res = 0

        l, r = 0, len(height) - 1
        while l < r:
            area = min(height[l], height[r]) * (r - l)
            res = max(res, area)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return res

s = Solution()
res = s.maxAreaTwoPointers([1,8,6,2,5,4,8,3,7])
print(res)

res = s.maxAreaTwoPointers([1,1])
print(res)