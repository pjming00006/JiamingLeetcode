"""
You are given an image represented by an m x n grid of integers image, where image[i][j] represents the pixel value of the image. You are also given three integers sr, sc, and color. Your task is to perform a flood fill on the image starting from the pixel image[sr][sc].

To perform a flood fill:

Begin with the starting pixel and change its color to color.
Perform the same process for each pixel that is directly adjacent (pixels that share a side with the original pixel, either horizontally or vertically) and shares the same color as the starting pixel.
Keep repeating this process by checking neighboring pixels of the updated pixels and modifying their color if it matches the original color of the starting pixel.
The process stops when there are no more adjacent pixels of the original color to update.
Return the modified image after performing the flood fill.



Example 1:

Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2

Output: [[2,2,2],[2,2,0],[2,0,1]]

Explanation:



From the center of the image with position (sr, sc) = (1, 1) (i.e., the red pixel), all pixels connected by a path of the same color as the starting pixel (i.e., the blue pixels) are colored with the new color.

Note the bottom corner is not colored 2, because it is not horizontally or vertically connected to the starting pixel.

Example 2:

Input: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, color = 0

Output: [[0,0,0],[0,0,0]]

Explanation:

The starting pixel is already colored with 0, which is the same as the target color. Therefore, no changes are made to the image.



Constraints:

m == image.length
n == image[i].length
1 <= m, n <= 50
0 <= image[i][j], color < 216
0 <= sr < m
0 <= sc < n
"""

from collections import deque

class Solution:
    def floodFillRecursionDFS(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        """
        DFS method with recursion.

        1. Start from image[sr][sc], take the value there and use it to evaluate if flood fill is necessary
        2. If image[m][n] == flood fill indicator, fill with new color
        3. Iterate through the 4 directions directly adjacent to the current node, until no further node is present

        Note: We need a visited matrix to store nodes already visited, to prevent infinite loops.
        Infinite loops happen when image[sr][sc] == color

        Time: O(m * n).
        Space: O(m * n). The visited matrix itself is O(m * n), the recursive stack is also O(m * n). Adding the 2 we have O(m * n)
        """
        m = len(image)
        n = len(image[0])
        flood_ind = image[sr][sc]
        visited = [[0 for i in range(n)] for j in range(m)]

        def recur(new_m, new_n):
            if visited[new_m][new_n] == 1:
                return
            if image[new_m][new_n] == flood_ind:
                image[new_m][new_n] = color
                visited[new_m][new_n] = 1
                if new_m > 0:
                    recur(new_m - 1, new_n)
                if new_m < m - 1:
                    recur(new_m + 1, new_n)
                if new_n > 0:
                    recur(new_m, new_n - 1)
                if new_n < n - 1:
                    recur(new_m, new_n + 1)

        recur(sr, sc)
        return image

    def floodFillRecursionDFSSimplified(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        """
        No need to create the visited matrix. If image[sr][sc] == color then we just return the original
        Time: O(m * n), Space: O(m * n)
        """
        m = len(image)
        n = len(image[0])
        flood_ind = image[sr][sc]

        if image[sr][sc] == color:
            return image

        def recur(new_m, new_n):
            if image[new_m][new_n] == flood_ind:
                image[new_m][new_n] = color
                if new_m > 0:
                    recur(new_m - 1, new_n)
                if new_m < m - 1:
                    recur(new_m + 1, new_n)
                if new_n > 0:
                    recur(new_m, new_n - 1)
                if new_n < n - 1:
                    recur(new_m, new_n + 1)

        recur(sr, sc)
        return image

    def floodFillDFSIteration(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        """
        No need to create the visited matrix. If image[sr][sc] == color then we just return the original
        Time: O(m * n)
        Space: O(m * n), because in thw worst case, the stack can grow to include every pixel in the largest connected component
        """
        m = len(image)
        n = len(image[0])
        flood_ind = image[sr][sc]

        if image[sr][sc] == color:
            return image

        stk = [[sr, sc]]

        while stk:
            current = stk.pop()
            new_m, new_n = current[0], current[1]
            if image[new_m][new_n] == flood_ind:
                image[new_m][new_n] = color
                if new_m > 0:
                    stk.append([new_m - 1, new_n])
                if new_m < m - 1:
                    stk.append([new_m + 1, new_n])
                if new_n > 0:
                    stk.append([new_m, new_n - 1])
                if new_n < n - 1:
                    stk.append([new_m, new_n + 1])
        return image


    def floodFillBFSIteration(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        """
        Time: O(m * n)
        Space: O(m * n), as the queue could grow to the size of the largest connected region in the image
        """
        m = len(image)
        n = len(image[0])
        flood_ind = image[sr][sc]

        if image[sr][sc] == color:
            return image

        queue = deque()
        queue.append([sr, sc])

        while queue:
            current = queue.popleft()
            new_m, new_n = current[0], current[1]
            if image[new_m][new_n] == flood_ind:
                image[new_m][new_n] = color
                if new_m > 0:
                    queue.append([new_m - 1, new_n])
                if new_m < m - 1:
                    queue.append([new_m + 1, new_n])
                if new_n > 0:
                    queue.append([new_m, new_n - 1])
                if new_n < n - 1:
                    queue.append([new_m, new_n + 1])
        return image



