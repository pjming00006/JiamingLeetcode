
class Solution:
    """
    The question specifies that division can not be used.

    """
    def find_solution(self, nums):
        left_p, right_p = [1] * len(nums), [1] * len(nums)
        for i in range(1, len(nums)):
            left_p[i] = left_p[i-1] * nums[i-1]

        for i in range(len(nums)-2, -1, -1):
            right_p[i] = right_p[i+1] * nums[i+1]

        res = [0] * len(nums)
        for i in range(len(nums)):
            res[i] = left_p[i] * right_p[i]
        return res

    def find_solution_space(self, nums):
        # This approach users O(1) space(excluding the result array)
        left_p, right_p = [1] * len(nums), [1] * len(nums)
        for i in range(1, len(nums)):
            left_p[i] = left_p[i - 1] * nums[i - 1]
        print(left_p)

        R = 1
        for i in reversed(range(len(nums))):
            print(i)
            left_p[i] = left_p[i] * R
            R = R * nums[i]
        return left_p
