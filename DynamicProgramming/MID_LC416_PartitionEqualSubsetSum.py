"""
Given an integer array nums, return true if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or false otherwise.



Example 1:

Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2:

Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.


Constraints:

1 <= nums.length <= 200
1 <= nums[i] <= 100
"""


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        """
        Top down dp with memorization
        """
        @lru_cache(maxsize=None)
        def get_sum(i, target_sum):
            if target_sum == 0:
                return True
            if i < 0:
                return False

            elif target_sum < 0:
                return False
            else:
                return get_sum(i - 1, target_sum - nums[i]) or get_sum(i - 1, target_sum)

        target = sum(nums) / 2
        if not target.is_integer():
            return False
        return get_sum(len(nums) - 1, int(target))


    def canPartitionBottomUpRecursion(self, nums: List[int]) -> bool:
        target = sum(nums) / 2
        if not target.is_integer():
            return False

        target = int(target)

        memo = {}

        def dp(i, cur_sum):
            # Finished processing the last element. Return false
            if i == len(nums):
                return False

            if (i, cur_sum) in memo:
                return memo[(i, cur_sum)]

            new_sum = cur_sum + nums[i]
            # find target, return True
            if new_sum == target:
                memo[(i, cur_sum)] = True
                return True

            # Less than target, go to next element
            if new_sum < target and dp(i + 1, new_sum):
                memo[(i, cur_sum)] = True
                return True

            # Greater than target, return
            if dp(i + 1, cur_sum):
                memo[(i, cur_sum)] = True
                return True

            memo[(i, cur_sum)] = False
            return False

        return dp(0, 0)

    def canPartitionBottomUp(self, nums: List[int]) -> bool:
        """
        We could maintain a 2-d array to memorize previous results - dp[i][sum]
        - i is the index, sum is the sum achievable. dp[i][sum] is boolean representing whether it is achieved
        """
        target = sum(nums) / 2
        if not target.is_integer():
            return False

        target = int(target)
        # Initialize 2-d array dp[i][sum]
        dp = [[False] * (target + 1) for i in range(len(nums))]

        # You can always achieve the first number from 0 just by adding the first number
        dp[0][0] = True

        for i in range(1, len(nums)):
            curr = nums[i]
            # For every sum from 0 to target
            for j in range(target + 1):
                # We can achieve it by 1 of the 2 ways
                # 1. Previous one with sum, not adding current
                # 2. Previous one with sum = sum - nums[i], adding the current
                if j < curr:
                    # If target sum is smaller than current, j - current < 0, we would get index out of range
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - curr]
        return dp[len(nums) - 1][target]

    def canPartition1dDP(self, nums: List[int]) -> bool:
        """
        We don't need the 2-D dp array, because we don't really care at which index we reached sum j. We only care if
        we could reach sum j or not.
        """
        target = sum(nums) / 2
        if not target.is_integer():
            return False

        target = int(target)
        # Initialize 2-d array dp[i][sum]
        dp = [False] * (target + 1)
        dp[0] = True
        for n in nums:
            for j in range(target, n - 1, -1):
                dp[j] = dp[j] or dp[j - n]
        return dp[target]
