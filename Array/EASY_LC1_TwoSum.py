"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.



Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]


Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.


Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
"""


class Solution:
    def twoSumBruteForce(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == target - nums[j]:
                    return [i, j]

    def twoSumHash(self, nums: list[int], target: int) -> list[int]:
        ht = {}
        for i in range(len(nums)):
            if target - nums[i] in ht.keys():
                return [ht[target - nums[i]], i]
            ht[nums[i]] = i


obj = Solution()
res = obj.twoSumHash([2, 7, 11, 15], 9)
print(res)

res = obj.twoSumHash([3, 2, 4], 6)
print(res)

res = obj.twoSumHash([3,3], 6)
print(res)

