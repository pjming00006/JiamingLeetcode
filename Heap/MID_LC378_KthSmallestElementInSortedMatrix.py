"""
Given an n x n matrix where each of the rows and columns is sorted in ascending order, return the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

You must find a solution with a memory complexity better than O(n2).



Example 1:

Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
Output: 13
Explanation: The elements in the matrix are [1,5,9,10,11,12,13,13,15], and the 8th smallest number is 13
Example 2:

Input: matrix = [[-5]], k = 1
Output: -5


Constraints:

n == matrix.length == matrix[i].length
1 <= n <= 300
-109 <= matrix[i][j] <= 109
All the rows and columns of matrix are guaranteed to be sorted in non-decreasing order.
1 <= k <= n2


Follow up:

Could you solve the problem with a constant memory (i.e., O(1) memory complexity)?
Could you solve the problem in O(n) time complexity? The solution may be too advanced for an interview but you may find reading this paper fun.
"""
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        """
        A brute force solution - does not leverage the property that each row and col is sorted
        """
        import heapq
        q = []

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                heapq.heappush(q, matrix[i][j])
                # Finding the kth smallest, so we can dump the bottom of the matrix
                if i > k and j > k:
                    break

        for i in range(k - 1):
            heapq.heappop(q)
        return q[0]

    def kthSmallestMinHeap(self, matrix: List[List[int]], k: int) -> int:
        import heapq
        q = []

        for i in range(len(matrix)):
            q.append((matrix[i][0], i, 0))

        heapq.heapify(q)

        while k > 0:
            cur_min, i, j = heapq.heappop(q)
            k -= 1

            if j < len(matrix[0]) - 1:
                heapq.heappush(q, (matrix[i][j + 1], i, j + 1))

        return cur_min

    def kthSmallestBinarySearch(self, matrix: List[List[int]], k: int) -> int:
        """
        In this binary search, we are not looking for a target, but to look for the len of left part until the len == k
        Since we are looking for the kth smallest, use the left part; if it's kth largest, we would use right part
        """
        R = len(matrix[0])
        left, right = matrix[0][0], matrix[R - 1][R - 1]

        while left < right:
            mid = (left + right) // 2
            left_cnt, left_max, right_min = 0, left, right
            i, j = R - 1, 0
            while i >= 0 and j < R:
                if matrix[i][j] <= mid:
                    left_cnt += 1 + i
                    left_max = max(left_max, matrix[i][j])
                    j += 1
                else:
                    right_min = min(right_min, matrix[i][j])
                    i -= 1

            if left_cnt == k:
                return left_max
            elif left_cnt < k:
                left = right_min
            else:
                right = left_max

        return left