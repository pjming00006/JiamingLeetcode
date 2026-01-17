class Solution:
    def robTopDown(self, nums: List[int]) -> int:
        memo = [-1] * len(nums)
        def backtrack(i):
            nonlocal memo
            if i >= len(nums):
                return 0
            if memo[i] != -1:
                return memo[i]
            # Option 1: skip this house and move to i+1
            skip_sum = backtrack(i+1)

            # Option 2: rob this house and move to i+2
            rob_sum = nums[i] + backtrack(i+2)
            
            memo[i] = max(skip_sum,rob_sum)
            return max(skip_sum,rob_sum)
        
        return backtrack(0)
    
    def robBottomUp(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        dp = [0] * len(nums)
        # Max from first house is always its own value
        # Max from house 1 is the max between nums[0] and nums[1]
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])
        
        return dp[-1]