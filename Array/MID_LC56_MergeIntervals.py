"""
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.



Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.


Constraints:

1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104
"""


class Solution:

    def mergeSorting(self, intervals: list[list[int]]) -> list[list[int]]:
        """
        If the input is not sorted then two arrays at any index can merge together. But if the input is sorted
        on the first index, then one array can only be merged with its previous arrays.(on a chain)

        Time: O(nlogn)
        Space: O(n)
        """
        intervals.sort(key=lambda x: x[0])
        merged = []
        for interval in intervals:
            if not merged or interval[0] > merged[-1][1]:
                merged.append(interval)
            else:
                merged[-1][1] = max(interval[1], merged[-1][1])
        return merged



s = Solution()
res = s.mergeSorting([[1,3],[2,6],[8,10],[15,18]])
print(res)

res = s.mergeSorting([[1,4],[4,5]])
print(res)


res = s.mergeSorting([[1,4],[0,2],[3,5]])
print(res)

