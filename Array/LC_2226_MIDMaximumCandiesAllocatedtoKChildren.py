class Solution:
    def maximumCandies(self, candies, k) -> int:
        num_candies = 0
        for pile in candies:
            num_candies += pile

        if num_candies < k:
            return 0

        cur_num = num_candies // k
        cur_k = k

        while cur_num > 0:
            for pile in candies:
                if pile < cur_num:
                    continue
                else:
                    cur_k = cur_k - (pile // cur_num)
            if cur_k <= 0:
                return cur_num
            else:
                cur_k = k
                cur_num -= 1

    def maximumCandies_binarySearch(self, candies, k) -> int:
        left = 1
        right = max(candies)

        cur_max = 0
        while left <= right:
            cur_k = k
            mid = (left + right) // 2
            print(f"current number: {mid}")
            for pile in candies:
                if pile < mid:
                    continue
                else:
                    cur_k = cur_k - (pile // mid)
            if cur_k <= 0:
                cur_max = max(cur_max, mid)
                left = mid + 1
            else:
                right = mid - 1
        return cur_max


test_case_1 = [5, 8, 6]
k1 = 3

s = Solution()
res = s.maximumCandies_binarySearch(candies=test_case_1, k=k1)
print(res)
