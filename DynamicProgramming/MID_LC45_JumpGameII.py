class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)

        @cache
        def find_step(i):
            if i >= n - 1:
                return 0  # Already at or past the last index

            min_jumps = float('inf')
            for j in range(1, nums[i] + 1):
                min_jumps = min(min_jumps, 1 + find_step(i + j))

            return min_jumps

        return find_step(0)

    def jumpGreedy(self, nums: List[int]) -> int:
        n = len(nums)
        cur_end = 0
        res = 0
        farthest = 0

        for i in range(n-1):
            step = nums[i]
            farthest = max(farthest, i+step)

            if i == cur_end:
                res += 1
                cur_end = farthest
        return res