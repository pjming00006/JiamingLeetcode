"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.



Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.


Constraints:

3 <= nums.length <= 3000
-105 <= nums[i] <= 105
"""


class Solution:
    def threeSumBruteForce(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i+1, len(nums)):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                for k in range(j+1, len(nums)):
                    if k > j + 1 and nums[k] == nums[k - 1]:
                        continue
                    if i != j and j != k and k != i and nums[i] + nums[j] + nums[k] == 0:
                        res.append([nums[i], nums[j], nums[k]])
        return res

    def threeSumBreakToTwoSum(self, nums: list[int]) -> list[list[int]]:
        """
        Trying to break down 3 sum into a 2 sum problem

        - First, sort the input
        - Loop through each element and use -nums[i] as the target to perform a 2 sum
        - If a triplet is found and the triplet is not in the result, add it

        Time: O(n^2)
            - The sorting itself is O(nlogn)
            - The 2 nested for loops are O(n^2)
            - Checking if the triplet is in res is O(k) where k is the current number of elements in res

            When n is large, O(nlogn) and O(k) become negligible and therefore we say time complexity is O(n^2)
        Space:
            - Sorting in place is O(1) and hashtable is O(n), therefore the operation is O(n)
        """
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            cur_target = -nums[i]
            ht = {}
            for j in range(i+1, len(nums)):
                # if j > i+1 and nums[j] == nums[j-1]:
                #     continue
                if cur_target - nums[j] in ht.keys():
                    triplet = [nums[i], cur_target - nums[j], nums[j]]
                    if triplet not in res:
                        res.append(triplet)
                ht[nums[j]] = j
        return res

    def threeSumTwoPointers(self, nums: list[int]) -> list[list[int]]:
        """
        Two Pointers

        Consider input [-1,0,1,2,-1,-4], after sorted: [-4, -1, -1, 0, 1, 2]

        - We initialize i at index 0 and treat the negative of the number as the target for 2 sum. Since array
            is sorted so we know that the first element is the smallest and the last is the largest.
        - Initialize left right pointer at i + 1 and len(nums) - 1
        - For each run, we calculate if nums[left] + nums[right] and evaluate:
            - If nums[left] + nums[right] < target, then we need a bigger element. Since the array is sorted we know
                that we need to increment left
            - If nums[left] + nums[right] > target, then we need a smaller element. Decrement right
            - If nums[left] + nums[right] > target, then we have an answer. Append the answer to the result.
                IMPORTANT: Now, we increment left and decrement right
        """
        nums.sort()
        res = []

        for i in range(len(nums)):
            # Avoid duplicates
            if i > 0 and nums[i] == nums[i-1]:
                continue

            left, right = i + 1, len(nums) - 1
            cur_target = -nums[i]
            while left < right:
                if nums[left] + nums[right] == cur_target:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1  # Skip duplicates for left
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1  # Skip duplicates for right
                elif nums[left] + nums[right] < cur_target:
                    left += 1
                else:
                    right -= 1
        return res


s = Solution()
res = s.threeSumTwoPointers([-1,0,1,2,-1,-4])
print(res)