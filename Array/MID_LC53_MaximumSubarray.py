"""
Given an integer array nums, find the subarray with the largest sum, and return its sum.



Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
Example 2:

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.


Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104


Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
"""


class Solution:
    """
    NOTES: This thought process is WRONG. But leave it here for future reflections
    ---Initial thought: Can I start with the whole array and decrease the subarray range as we go?
        Evaluation 1: we exclude it if the number is a minus
            NOT WORKING ON ITS OWN. E.g.: [-2,1,-3,4,-1,2,1,-5,4], we start with the whole thing and we exclude -2
            because it's a minus. But now we have 1 and 4, which are both positive
        Evaluation 2: we compare number on left with left + 1, right with right - 1. If including both is not worth it
        then we exclude.
            E.g.: [-2,1,-3,4,-1,2,1,-5,4],
                1. we compare -2 and 1, -5 and 4. Both results are -1, so exclude left
                2. we compare 1 and -3, -5 and 4. Left is -2 and right is -1. Exclude left
                3. we compare -3 and 4, -5 and 4. Left is 1 and right is -1. Exclude right
                4. we compare -3 and 4, 1 and -5. Left is 1 and right is -4. Exclude right
                5. we compare -3 and 4, 2 and 1. Left is 1 and right is 3.
                   - Based on the evaluation both should stay. But if we combine with evaluation 1, we can exclude
                     the left because it is minus.

        Conclusion: we should use both evaluation metrics.

        Edge cases:
            1. What if there are only 2 elements, and 1 of them is negative
            2. What if there are only 2 elements, and both of them are negative
    """

    def maxSubArrayBruteForce(self, nums: list[int]) -> int:
        ans = nums[0]
        for i in range(len(nums)):
            cur_sum = 0
            for j in range(i, len(nums)):
                cur_sum += nums[j]
                ans = max(ans, cur_sum)
        return ans


    def maxSubArrayKanade(self, nums: list[int]) -> int:
        """
        Dynamic programming: finding the SUB-PROBLEM.
        How do we know the maximum subarray at a given index i?
            - It is either itself, or the maximum subarray at nums[i-1] plus nums[i]

        Time: O(n). We traverse the array 1 time
        Space: O(1): Additional constant space is used
        """
        max_ending_here = nums[0]
        max_so_far = nums[0]
        for i in range(1, len(nums)):
            max_ending_here = max(max_ending_here + nums[i], nums[i])
            max_so_far = max(max_ending_here, max_so_far)
        return max_so_far

    def maxSubArrayRecurssion(self, nums: list[int]) -> int:
        """
        Recursion using the Kanade algorithm

        - We start from the last index and going back the array
        - The maximum subarray is either the current element by itself or the maximum subarray of nums[i-1] + nums[i]
        - The stop condition is index == 0, where the max_ending_here and max_so_far are just the element itself
        - Then, recursively, update the max_ending_here as either the element or element + maximum subarray of i-1
        - If max_ending_here is greater than max_so_far, update max_so_far
        """
        def solve(index, max_so_far):
            if index == 0:
                return nums[index], nums[index]
            else:
                max_ending_here, max_so_far = solve(index-1, max_so_far)
                max_ending_here = max(max_ending_here + nums[index], nums[index])
                max_so_far = max(max_so_far, max_ending_here)
                return max_ending_here, max_so_far

        return solve(len(nums)-1, -105)[1]

    def maxSubArrayTwoPointers(self, nums: list[int]) -> int:
        """
        THIS DOES NOT WORK!!!!!
        Leave here as a bad example.
        I tried to evaluate each element by itself, or to evaluate the elements next to it.
        For example, if the element is negative, exclude it, or if the next element contributes more negatively than
        this element positively, then exclude.

        But this approach does not deal with situations where consecutive negative values exists

        WE HAVE TO CONSIDER ALL THE SUB-ARRAYS, NOT JUST ONE OR TWO ELEMENTS.
        """
        if len(nums) == 1:
            return sum(nums)

        l, r = 0, len(nums) - 1

        while l < r:
            if nums[l] < 0 and nums[l] < nums[r]:
                l += 1
            elif nums[r] < 0 and nums[r] < nums[l]:
                r -= 1
            elif nums[l] + nums[l+1] < 0:
                l += 1
            elif nums[r] + nums[r-1] < 0:
                r -= 1
            else:
                return sum(nums[l: r + 1])
        return sum(nums[l: r + 1])


obj = Solution()
res = obj.maxSubArrayRecurssion([-2,1,-3,4,-1,2,1,-5,4])
print(res)

res = obj.maxSubArrayRecurssion([5,4,-1,7,8])
print(res)

res = obj.maxSubArrayRecurssion([-2,1])
print(res)

res = obj.maxSubArrayRecurssion([-1,-2])
print(res)

res = obj.maxSubArrayRecurssion([31,-41,59,26,-53,58,97,-93,-23,84])
print(res)
