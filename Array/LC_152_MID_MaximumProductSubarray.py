
class Solution:
    """
    The question specifies that division can not be used.

    """
    def find_solution_bruteforce(self, nums):
        if len(nums) == 0:
            return 0

        max_p = nums[0]
        for i in range(len(nums)):
            cur_prod = 1
            for j in range(i, len(nums)):
                cur_prod = cur_prod * nums[j]
                max_p = max(max_p, cur_prod)

        return max_p
    
    def find_solution_dynamic(self, nums):
        if len(nums) == 0:
            return 0

        cur_max = nums[0]
        cur_min = nums[0]
        max_prod = nums[0]
        for i in range(1, len(nums)):
            curr = nums[i]
            temp_max = max(curr, cur_max * curr, cur_min * curr)
            cur_min = min(curr, cur_max * curr, cur_min * curr)

            cur_max = temp_max
            max_prod =  max(max_prod, cur_max)
        return max_prod
