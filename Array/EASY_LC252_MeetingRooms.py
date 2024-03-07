"""
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all meetings.

Example 1:

Input: [[0,30],[5,10],[15,20]]
Output: false
Example 2:

Input: [[7,10],[2,4]]
Output: true
"""


class Solution:
    """
    Related problems: LC56, LC435
    """
    def canAttendMeetings(self, intervals: list[list[int]]) -> bool:
        """
        Time: O(nlogn): sort + linear traversal
        Space: O(1)
        """
        intervals.sort(key=lambda x: x[0])

        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[i-1][1]:
                return False

        return True

s = Solution()
res = s.canAttendMeetings([[0,30],[5,10],[15,20]])
print(res)

res = s.canAttendMeetings([[7,10],[2,4]])
print(res)