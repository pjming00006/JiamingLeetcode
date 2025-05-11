"""
Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

The distance between two cells sharing a common edge is 1.



Example 1:


Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
Output: [[0,0,0],[0,1,0],[0,0,0]]
Example 2:


Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
Output: [[0,0,0],[0,1,0],[1,2,1]]


Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 104
1 <= m * n <= 104
mat[i][j] is either 0 or 1.
There is at least one 0 in mat.
"""


class Solution:
    def updateMatrixBFS(self, mat: List[List[int]]) -> List[List[int]]:
        """
        BFS:
        - First, find all zeros in the matrix. Their shortest distance is 0
        - Then, put the zero elements into a queue
        - Start FIFO, update the elements around the current element; ignore if already visited
        - Once update is done, put the updated element into the queue
        """
        from collections import deque

        def is_valid(i, j) -> bool:
            return 0 <= i < R and 0 <= j < C

        R, C = len(mat), len(mat[0])
        visited = [[0 for j in range(C)] for i in range(R)]

        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        q = deque()
        for i in range(R):
            for j in range(C):
                if mat[i][j] == 0:
                    visited[i][j] = 1
                    q.append((i, j, 0))

        while q:
            i, j, dist = q.popleft()
            # move up is possible and up element is not visited
            for direction in directions:
                next_i, next_j = direction[0] + i, direction[1] + j
                if is_valid(next_i, next_j) and visited[next_i][next_j] == 0:
                    visited[next_i][next_j] = 1
                    mat[next_i][next_j] = dist + 1
                    q.append((next_i, next_j, dist + 1))
        return mat

    def updateMatrixDynamicProgramming(self, mat: List[List[int]]) -> List[List[int]]:
        """
        Intuition:
        To find the distance for any element, we just need to take the minimum distance of the 4 adjacent elements and
        plus 1. So, finding any element's distance is to find the distance of the adjacent element

        The issue is that we cannot just randomly check the 4 directions as it would end up being infinite loop.
        Therefore, we could implement 2 loops:
        1. From top left to bottom right, for each element, check the left and up elements and find minimum
        2. From bottom right to top left, for each element, check the right and down elements, find min, compare, with
           results in (1)
        """
        R, C = len(mat), len(mat[0])
        res = [row for row in mat]

        for i in range(R):
            for j in range(C):
                if mat[i][j] != 0:
                    minLast = inf
                    if i > 0:
                        minLast = min(minLast, res[i - 1][j])
                    if j > 0:
                        minLast = min(minLast, res[i][j - 1])

                    res[i][j] = minLast + 1

        for i in range(R - 1, -1, -1):
            for j in range(C - 1, -1, -1):
                if res[i][j] != 0:
                    minLast = inf
                    if i < R - 1:
                        minLast = min(minLast, res[i + 1][j])
                    if j < C - 1:
                        minLast = min(minLast, res[i][j + 1])

                    res[i][j] = min(res[i][j], minLast + 1)

        return res