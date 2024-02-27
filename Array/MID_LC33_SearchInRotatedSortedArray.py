"""
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.



Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Example 3:

Input: nums = [1], target = 0
Output: -1


Constraints:

1 <= nums.length <= 5000
-104 <= nums[i] <= 104
All values of nums are unique.
nums is an ascending array that is possibly rotated.
-104 <= target <= 104
"""


class Solution:
    def searchBruteForce(self, nums: list[int], target: int) -> int:
        # Brute force. This solution IS NOT O(log n)
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        return -1

    def searchBruteForceBinary(self, nums: list[int], target: int) -> int:
        """
        Find the break-out point, then define mid, then binary search
        1. Loop through index 1 to len(nums), if nums[i] < nums[i-1], then i is the smallest element, break the loop
        2. Create a mapping of normal sorted array indexes to this rotated indexes
        3. Do binary search on the mapping

        This solution IS NOT O(log n)
        """
        start_ind = 0
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                start_ind = i
                break

        bs_inx = {}

        cur_inx = 0
        for j in range(start_ind, len(nums)):
            bs_inx[cur_inx] = j
            cur_inx += 1
        for x in range(0, start_ind):
            bs_inx[cur_inx] = x
            cur_inx += 1

        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            print(nums[bs_inx[mid]])
            if nums[bs_inx[mid]] == target:
                return bs_inx[mid]
            elif nums[bs_inx[mid]] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1


    def searchRevisedBinarySearch(self, nums: list[int], target: int) -> int:
        """
        No matter what the cutoff is, when we are at a certain element in the array, there is always one side
        (left or right) or the subarray is fully-sorted

        1. Find mid
        2. Compare mid with left and right to figure out which side is fully sorted
        3. On the fully sorted side, compare and see if target is within left & right boundaries
        4. If it is, then binary search the fully-sorted side; if not, binary search the other side
        """
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            elif nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1


obj = Solution()
res = obj.searchRevisedBinarySearch([4,5,6,7,0,1,2], 0)
print(res)

res = obj.searchRevisedBinarySearch([4,5,6,7,0,1,2], 3)
print(res)

res = obj.searchRevisedBinarySearch([1], 2)
print(res)


