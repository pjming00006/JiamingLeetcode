"""
Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.



Example 1:

Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.
Example 2:

Input: intervals = [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.
Example 3:

Input: intervals = [[1,2],[2,3]]
Output: 0
Explanation: You don't need to remove any of the intervals since they're already non-overlapping.


Constraints:

1 <= intervals.length <= 105
intervals[i].length == 2
-5 * 104 <= starti < endi <= 5 * 104
"""


class Solution:
    """
    Initial thoughts:
    - This is related to LC56 - merging intervals, where we used sorting to simplify the problem
        In LC56, we were trying to merge as many intervals and possible

    - For this problem, it's natural to think about criteria to remove some intervals so that the remaining is
        non-overlapping. But, a simpler way is to think about a criteria to retain the MOST non-overlapping intervals

        * Minimum number of intervals to remove to make the rest of intervals non-overlapping
          ==
          Find the maximum number of non-overlapping intervals


        BUT HOW?
        We increment a count once we meet an interval that does not overlap with the preceding one by comparing the
        ending element of the previous interval with the starting element of the current interval. When there is no
        overlap, we update the ending element for future comparison. When there is overlap, we keep the original ending
        value

        To do this, we need to change the way we sort. WHY?
        Consider an input: [[1,100],[11,22],[1,11],[2,12]]

        We can follow what we did in LC56 - sort asc for the starting element
            - [[1, 100], [1, 11], [2, 12], [11, 22]]
            If we sort this way and follow similar approach, we find that [1, 100] can actually merge with ALL
            the following intervals. As a result, the maximum number of non-overlapping intervals would be SMALL

        Or, we can sort asc for the ending element
            - [[1, 11], [2, 12], [11, 22], [1, 100]]
            In this case, [2, 12] is overlapping with [1, 11], but [11, 22] is NOT overlapping with [1, 11]
            and [1, 100] is overlapping with [11, 22]
        https://leetcode.com/problems/non-overlapping-intervals/solutions/276056/python-greedy-interval-scheduling/

    """
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        """
        Time: O(nlogn) sort + linear traversal
        Space: O(1)
        """
        intervals.sort(key=lambda x: x[1])

        cnt = 1
        cur_end = intervals[0][1]
        for i in range(len(intervals)):
            if intervals[i][0] >= cur_end:
                cnt += 1
                cur_end = intervals[i][1]

        return len(intervals) - cnt


s = Solution()
res = s.eraseOverlapIntervals([[1,100],[11,22],[1,11],[2,12]])
print(res)
