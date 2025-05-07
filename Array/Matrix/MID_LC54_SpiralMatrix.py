"""
Given an m x n matrix, return all elements of the matrix in spiral order.



Example 1:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:


Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]


Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100
"""

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        visited = [[0 for j in range(len(matrix[0]))] for i in range(len(matrix))]
        element_cnt = len(matrix) * len(matrix[0])

        res = []
        i, j, cnt, cur_direction = 0, 0, 0, 0

        while cnt < element_cnt:
            curr = matrix[i][j]
            if visited[i][j] == 0:
                visited[i][j] = 1
                cnt += 1
                res.append(curr)

            # Move right
            if cur_direction == 0:
                if j+1 < len(matrix[0]) and visited[i][j+1] == 0:
                    j += 1
                else:
                    cur_direction += 1
            # Move down
            if cur_direction == 1:
                if i+1 < len(matrix) and visited[i+1][j] == 0:
                    i += 1
                else:
                    cur_direction += 1
            # Move left
            if cur_direction == 2:
                if j-1 >= 0 and visited[i][j-1] == 0:
                    j -= 1
                else:
                    cur_direction += 1
            # Move up
            if cur_direction == 3:
                if i-1 >= 0 and visited[i-1][j] == 0:
                    i -= 1
                else:
                    cur_direction = 0
        return res

    def spiralOrderImproved(self, matrix: List[List[int]]) -> List[int]:
        """
        This approach has several improvements:
        1. No need to initialize a new matrix to store visited elements as we could do it in-place
        2. No need to maintain a count to know when to stop. If direction is changed twice, it's time to stop
        """
        res = [matrix[0][0]]
        # Mark visited element in place because we would never use it again
        visited = 101
        matrix[0][0] = visited

        # Move right, down, left, up
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        R, C = len(matrix), len(matrix[0])
        i, j = 0, 0
        change_direction_cnt = 0
        current_direction = 0

        while change_direction_cnt < 2:
            while True:
                # Next index
                i1, j1 = i + directions[current_direction][0], j + directions[current_direction][1]

                if i1 >= R or i1 < 0 or j1 >= C or j1 < 0:
                    break

                if matrix[i1][j1] == visited:
                    break

                change_direction_cnt = 0
                i, j = i1, j1
                res.append(matrix[i][j])
                matrix[i][j] = visited

            change_direction_cnt += 1
            current_direction = (current_direction + 1) % 4
        return res