"""
Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.



Example 1:


Input: n = 3
Output: [[1,2,3],[8,9,4],[7,6,5]]
Example 2:

Input: n = 1
Output: [[1]]


Constraints:

1 <= n <= 20
"""


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0 for j in range(n)] for i in range(n)]
        not_visited = 0
        res[0][0] = 1

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        current_direction = 0
        change_direction_cnt = 0

        R, C = n, n
        i, j = 0, 0

        while change_direction_cnt < 2:
            while True:
                i1, j1 = i + directions[current_direction][0], j + directions[current_direction][1]

                if i1 >= R or i1 < 0 or j1 >= C or j1 < 0:
                    break
                if res[i1][j1] != not_visited:
                    break

                change_direction_cnt = 0
                val = res[i][j] + 1
                i, j = i1, j1
                res[i][j] = val

            current_direction = (current_direction + 1) % 4
            change_direction_cnt += 1
        return res