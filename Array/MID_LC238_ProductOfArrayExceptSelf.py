"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.



Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]


Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.


Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)
"""
class Solution:
    def productExceptSelfBruteForce(self, nums: list[int]) -> list[int]:
        """
        Since we can't use division, it is natural to think that we can multiply all the remaining elements in the
        array. So the brute force way is easy: for each element, loop through the rest of elements and multiply.
        """
        res = []
        for i in range(len(nums)):
            prd = 1
            for j in range(len(nums)):
                if i == j:
                    continue
                else:
                    prd = prd * nums[j]
            res.append(prd)
        return res

    def productExceptSelfTwoArrays(self, nums: list[int]) -> list[int]:
        """
        Thinking 1 step further, we can find that the parts of the operation from the brute force solution can
        be re-used - we don't have to loop through every other elements and multiply them; instead, we can simplify
        the problem as multiply the product of the left side of array with the product of the right side of the array.
        """
        l_prd, r_prd = [1] * len(nums), [1] * len(nums)

        for i in range(1, len(nums)):
            l_prd[i] = l_prd[i-1] * nums[i-1]
        for j in range(len(nums)-2, -1, -1):
            r_prd[j] = r_prd[j+1] * nums[j+1]
        res = [1] * len(nums)
        for n in range(len(nums)):
            res[n] = l_prd[n] * r_prd[n]
        return res


    def productExceptSelfOneArray(self, nums):
        """
        Reflecting on the 2-array solution, we can find that it is not necessary to have a right product array.
        We know that for the first&last element, the product on the left/right-hand side is always 1. Therefore,
        we can always start by declaring 1 for the product, then multiply the current element in the array to update
        the product. In that way, we only use O(1) additional space.
        """
        l_prd = [1] * len(nums)
        r_prd = 1
        for i in range(1, len(nums)):
            l_prd[i] = l_prd[i-1] * nums[i-1]
        for j in range(len(nums)-1, -1, -1):
            l_prd[j] = l_prd[j] * r_prd
            r_prd = r_prd * nums[j]
        return l_prd

obj = Solution()
res = obj.productExceptSelfOneArray([1,2,3,4])
print(res)

res = obj.productExceptSelfOneArray([-1,1,0,-3,3])
print(res)
