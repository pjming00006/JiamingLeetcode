"""
There are n people standing in a queue, and they numbered from 0 to n - 1 in left to right order. You are given
an array heights of distinct integers where heights[i] represents the height of the ith person.

A person can see another person to their right in the queue if everybody in between is shorter than both of them.
More formally, the ith person can see the jth person if i < j and
min(heights[i], heights[j]) > max(heights[i+1], heights[i+2], ..., heights[j-1]).

Return an array answer of length n where answer[i] is the number of people the ith person
can see to their right in the queue.


Example 1:

Input: heights = [10,6,8,5,11,9]
Output: [3,1,2,1,1,0]
Explanation:
Person 0 can see person 1, 2, and 4.
Person 1 can see person 2.
Person 2 can see person 3 and 4.
Person 3 can see person 4.
Person 4 can see person 5.
Person 5 can see no one since nobody is to the right of them.
Example 2:

Input: heights = [5,1,2,3,10]
Output: [4,1,1,1,0]


Constraints:

n == heights.length
1 <= n <= 105
1 <= heights[i] <= 105
All the values of heights are unique.
"""


class Solution:
    def canSeePersonsCountBruteForce(self, heights: list[int]) -> list[int]:
        """
        Observation:
        1. We should start from the end and try to remember the elements we visited
        2. If one element is higher than all elements on the right, then everything on the right is useless and can
           be discarded
        3. If height[i] < height[i+1], then answer is constant at 1
        4. If height[i] > height[i+1], then we need to count how many people we can see

        Time: O(n^2)
        Space: O(1)
        """
        res = [1] * len(heights)
        res[-1] = 0

        def check_counts(cur_height: int, q: list[int]):
            if not q:
                return 0
            if cur_height < q[0]:
                return 1
            else:
                cnt = 0
                cur_max = 0
                for j in range(len(q)):
                    if cur_height < q[j]:
                        cnt += 1
                        return cnt
                    else:
                        if q[j] > cur_max:
                            cnt += 1
                            cur_max = max(cur_max, q[j])
                return cnt

        for i in range(len(heights)-1, -1, -1):
            res[i] = check_counts(heights[i], heights[i+1:])
        return res

    def canSeePersonsCountStack(self, heights: list[int]) -> list[int]:
        """
        We can use a stack to track the list of people a particular person can see

        Iteration flow:
        1. Count length of stack
        2. While current element is larger than the stack, pop the stack
        3. add current to the stack

        Time: O(n)
        Space: O(n)
        """
        stack = []
        res = [0] * len(heights)

        for i in range(len(heights)-1, -1, -1):
            if not stack:
                res[i] = 0
            else:
                cnt = 0
                while stack and heights[i] > stack[-1]:
                    stack.pop()
                    cnt += 1
                if stack:
                    cnt += 1
                res[i] = cnt
            stack.append(heights[i])
            # print(f"number: {heights[i]}, stack: {stack}")

        return res



s = Solution()
# res = s.canSeePersonsCountStack([10,6,8,5,11,9])
# print(res)

# res = s.canSeePersonsCountStack([5,1,2,3,10])
# print(res)

res = s.canSeePersonsCountStack([3,1,5,8,6])
print(res)