"""
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?



Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4


Constraints:

1 <= k <= nums.length <= 105
-104 <= nums[i] <= 104
"""


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq

        q = []

        for n in nums:
            heapq.heappush(q, n)
            if len(q) > k:
                heapq.heappop(q)

        return q[0]

    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quick_select(nums, k):
            pivot = random.choice(nums)
            left, mid, right = [], [], []

            for n in nums:
                if n > pivot:
                    left.append(n)
                elif n == pivot:
                    mid.append(n)
                else:
                    right.append(n)

            # If left has more than k elements, the kth must be within left
            if len(left) >= k:
                return quick_select(left, k)
            elif len(left) + len(mid) < k:
                return quick_select(right, k - (len(left) + len(mid)))
            return pivot

        return quick_select(nums, k)
