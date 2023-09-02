import math
class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        # Minimum possible number would be 1 banana at a time, max is the biggest pile
        left = 1
        right = max(piles)

        res = right
        while left <= right:
            mid = (left + right) // 2
            cur_h = h

            for pile in piles:
                cur_h -= math.ceil(pile / mid)
            if cur_h >= 0:
                right = mid - 1
                res = min(res, mid)
            else:
                left = mid + 1
        return res


s = Solution()
test = [30,11,23,4,20]
h = 5

res = s.minEatingSpeed(test, h)
print(res)
