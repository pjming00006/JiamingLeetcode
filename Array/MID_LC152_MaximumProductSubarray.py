"""
Given an integer array nums, find a subarray that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.



Example 1:

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.


Constraints:

1 <= nums.length <= 2 * 104
-10 <= nums[i] <= 10
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
"""
class Solution:
    def maxProductBruteForce(self, nums: list[int]) -> int:
        if len(nums) == 0:
            return 0

        max_p = nums[0]
        for i in range(len(nums)):
            cur_prod = 1
            for j in range(i, len(nums)):
                cur_prod = cur_prod * nums[j]
                max_p = max(max_p, cur_prod)

        return max_p

    def maxProductKanade(self, nums: list[int]) -> int:
        """
        Kanade Algorithm.
        The maximum product subarray ending at current index i is always either itself, or the element multiply by the
        maximum product subarray at index i-1.

        Issues to watch out:
        1. Since this question asks about the product - if current element is negative, then we need to get the max
            product by using the prior minimum. Therefore, we need to track BOTH the max so far and min so far
        2. To get max and min, we need to compare 3 values:
            (1) Current element
            (2) prior max * current element
            (3) prior min * current element
            Since (2) and (3) both use max and min so far, we need a temp field storing the original value before
            it gets overwritten.
        """
        if len(nums) == 0:
            return 0

        max_so_far, max_ending_here, min_ending_here = nums[0], nums[0], nums[0]
        for i in range(1, len(nums)):
            # print(f"number: {nums[i]}")
            temp_max_ending_here = max(max_ending_here * nums[i], min_ending_here * nums[i], nums[i])
            min_ending_here = min(max_ending_here * nums[i], min_ending_here * nums[i], nums[i])
            max_ending_here = temp_max_ending_here
            max_so_far = max(max_ending_here, max_so_far)
            # print(max_so_far, max_ending_here, min_ending_here)
        return max_so_far

    def maxProductKanadeSimplified(self, nums: list[int]) -> int:
        """
        Kanade Simplified
        - When we encounter a negative value, max becomes min and min becomes max, so we can swap
        """
        if len(nums) == 0:
            return 0

        max_so_far, max_ending_here, min_ending_here = nums[0], nums[0], nums[0]
        for i in range(1, len(nums)):
            # print(f"number: {nums[i]}")
            if nums[i] < 0:
                temp_max_ending_here = max_ending_here
                max_ending_here = min_ending_here
                min_ending_here = temp_max_ending_here

            max_ending_here = max(max_ending_here * nums[i], nums[i])
            min_ending_here = min(min_ending_here * nums[i], nums[i])
            max_so_far = max(max_ending_here, max_so_far)
            # print(max_so_far, max_ending_here, min_ending_here)
        return max_so_far

    def maxProductTwoPointers(self, nums: list[int]) -> int:
        """
        Subtle solution - divide and conquer

        - Have 2 pointers one moving from start and the other moving from end of array
        - Each iteration, left and right move toward each other and compute product
        - If left product or right product encounter odd number of negative values, they would turn negative and likely
            drop out of the sum; when there are even number of negative values, they will become positive again, so
            the looping itself sets the cutting point
        - If the current value left or right pointing at is 0, then we reset the product to 1, representing a cutoff
        """

        left_product, right_product = 1, 1
        ans = nums[0]
        l, r = 0, len(nums) - 1
        for n in range(len(nums)):
            if left_product == 0:
                left_product = 1
            if right_product == 0:
                right_product = 1
            left_product *= nums[l]
            right_product *= nums[r]

            ans = max(left_product, right_product, ans)

            l += 1
            r -= 1
        return ans




obj = Solution()
res = obj.maxProductTwoPointers([-4,-3,-2])
print(res)

res = obj.maxProductTwoPointers([-2,0,-1])
print(res)

res = obj.maxProductTwoPointers([2,3,-2, 4])
print(res)
