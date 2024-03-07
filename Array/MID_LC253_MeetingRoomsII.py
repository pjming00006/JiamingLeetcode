"""
Given an array of meeting time intervals consisting of start and end times[[s1,e1],[s2,e2],...](si< ei), find the minimum number of conference rooms required.

Example 1:
Input:
[[0, 30],[5, 10],[15, 20]]
Output: 2

Example 2:
Input:
[[7,10],[2,4]]

Output: 1
"""

class Solution:
    """
    Related problems: LC56, LC435, LC252

    Different from LC56, LC435 and LC252, this problem requires us to know where previous intervals end

    A good method would be a priority queue, but I don't know about it so forget it for now
    """
    def findNumberOfRooms(self, intervals: list[list[int]]) -> int:
        """
        - Extract the start and end times into separate strings and sort them asc
        - Initialize 2 pointers from index 0
        - If start_times[start_ind] < end_times[end_ind], it indicates a new meeting is starting before another meeting
            has concluded, thereby requiring an additional room. Thus, active is incremented, and start_ind
            is moved to the next meeting start time.
        - If start_times[start_ind] >= end_times[end_ind], it suggests a meeting has concluded (or ends right when
            another begins), and hence a room is freed. In this case, we move to the next end time by incrementing
            end_ind. Note that active is not decremented here because the comparison logic implicitly handles the
            balance between meetings starting and ending without explicitly needing to decrement the count of active rooms.
        """
        start_times, end_times = [0] * len(intervals) , [0] * len(intervals)
        for i in range(len(intervals)):
            start_times[i], end_times[i] = intervals[i][0], intervals[i][1]

        start_times.sort()
        end_times.sort()

        start_ind, end_ind = 0, 0
        active = 0
        res = 0

        while start_ind < len(intervals) and end_ind < len(intervals):
            if start_times[start_ind] < end_times[end_ind]:
                active += 1
                start_ind += 1
            else:
                active -= 1
                end_ind += 1

            res = max(res, active)

        return res


s = Solution()
res = s.findNumberOfRooms([[0,30],[5,10],[15,20]])
print(res)

res = s.findNumberOfRooms([[7,10],[2,4]])
print(res)

res = s.findNumberOfRooms([[1,100],[1,11], [2,12], [11,22], [20,25]])
print(res)