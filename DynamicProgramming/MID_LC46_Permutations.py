class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(perm):
            nonlocal nums, res

            if len(perm) == len(nums):
                res.append(perm.copy())
                return

            for n in nums:
                if n not in perm:
                    perm.append(n)
                    backtrack(perm)
                    perm.pop()