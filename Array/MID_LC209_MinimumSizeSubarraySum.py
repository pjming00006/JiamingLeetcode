"""
Given an array of positive integers nums and a positive integer target, return the minimal length of a
subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.



Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1
Example 3:

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0


Constraints:

1 <= target <= 109
1 <= nums.length <= 105
1 <= nums[i] <= 104


Follow up: If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log(n)).
"""


class Solution:
    def minSubArrayLenBruteForce(self, target: int, nums: list[int]) -> int:
        """
        Brute Force
        1. Set the answer to be length of array + 1
        2. Nested for loop - for each element, find all combinations of subarray, adding up the sum
        3. If the sum exceeds the target, compare and get the smallest length
        4. When done, if ans == len(nums) + 1, which means no possible subarray found, then we return 0
        5. Otherwise, we return the smallest subarray
        """
        ans = len(nums) + 1
        for i in range(len(nums)):
            cur_sum = 0
            for j in range(i, len(nums)):
                cur_sum += nums[j]
                if cur_sum >= target:
                    ans = min(ans, j-i+1)
                    break
        if ans > len(nums):
            return 0
        return ans


    def minSubArrayLenSlidingWindow(self, target: int, nums: list[int]) -> int:
        """
        1. Initialize left and right at the start of array
        2. We go through each element and add it to the sum.
        3. If sum reaches target, we start to pop the left element until the sum is less than target
        4. Then we continue to loop to the right to find the smallest number
        """
        left, right = 0, 0
        ans = len(nums) + 1
        cur_sum = 0

        for right in range(len(nums)):
            cur_sum += nums[right]
            while cur_sum >= target:
                ans = min(ans, right-left+1)
                cur_sum -= nums[left]
                left += 1
        if ans > len(nums):
            return 0
        return ans


    def minSubArrayLenBinarySearch(self, target: int, nums: list[int]) -> int:
        """
        If we create a new array storing the sum of subarray ending at each element in the corresponding index of the
        new array, then it turns out that the sums array is sorted.
        E.g. [2,3,1,2,4,3] -> [2,5,6,8,12,15]

        Now, if we do sums[3] - sums[0], we are calculating the sum of subarray from index 0 to index 3
        - (8 - 2 = 6) --> 2 + 3 + 1 = 6

        With the 2 understandings above, if we are evaluating a number at index j for each index i, we just need to
        compare if nums[j] - nums[i] >= target, or nums[j] >= target - nums[i]

        Now, the problem becomes a binary search problem within a for loop:
        1. Loop through input to calculate sums ending at each index
        2. For each index in len(sums), we do a binary search trying to find the index j where
            nums[j] - nums[i] >= target
        3. If we find it, update ans
        4. Loop through the rest of the array

        Note: For cases where target = 15, nums = [1,2,3,4,5], the length of the whole array is the answer
              We need to add a 0 in front of the sums array to represent the sums of all previous subarray elements
              ending at index 0.

        """
        sums = [0] * (len(nums) + 1)
        ans = len(nums) + 1
        for i in range(len(nums)):
            sums[i+1] = sums[i] + nums[i]
        # print(sums)

        for j in range(len(sums)):
            left = j
            right = len(sums) - 1
            while right >= left:
                mid = (left + right) // 2
                # print(j, left, right, mid)
                # print(sums[mid] - sums[j])
                if sums[mid] - sums[j] < target:
                    left = mid + 1
                else:
                    ans = min(ans, mid-j)
                    # print(f"new ans: {ans}")
                    right = mid - 1
        if ans > len(nums):
            return 0
        return ans


s = Solution()
res = s.minSubArrayLenBinarySearch(7, [2,3,1,2,4,3])
print(res)

res = s.minSubArrayLenBinarySearch(4, [1,4,4])
print(res)

res = s.minSubArrayLenBinarySearch(11, [1,1,1,1,1,1,1,1])
print(res)

res = s.minSubArrayLenBinarySearch(15, [1,2,3,4,5])
print(res)
