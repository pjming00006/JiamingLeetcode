"""
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.



Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Example 2:

Input: nums = [2,0,1]
Output: [0,1,2]


Constraints:

n == nums.length
1 <= n <= 300
nums[i] is either 0, 1, or 2.


Follow up: Could you come up with a one-pass algorithm using only constant extra space?
"""


class Solution:
    def sortColorsCountingSort(self, nums: list[int]) -> None:
        """
        Counting sort:
        Time: O(n)
        Space: O(n)
        """

        cnts = [0, 0, 0]

        for n in nums:
            cnts[n] += 1
        for i in range(1, len(cnts)):
            cnts[i] = cnts[i-1] + cnts[i]

        res = [0] * len(nums)
        for j in range(len(nums)):
            current = nums[j]
            cur_ind = cnts[current] - 1
            res[cur_ind] = current
            cnts[current] -= 1
        nums = res
        print(nums)

    def sortColorsDutchNationalFlag(self, nums: list[int]) -> None:
        """
        Counting sort:
        Time: O(n)
        Space: O(1)
        1-pass solution
        """

        low, mid, high = 0, 0, len(nums) - 1
        while mid <= high:
            if nums[mid] == 0:
                nums[mid], nums[low] = nums[low], nums[mid]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
        print(nums)


s = Solution()
s.sortColorsDutchNationalFlag([2,0,2,1,1,0])
s.sortColorsDutchNationalFlag([2,0,1])
s.sortColorsDutchNationalFlag([1,2,0])



