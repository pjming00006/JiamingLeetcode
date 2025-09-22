"""
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.



Example 1:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
Example 2:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true
Example 3:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false


Constraints:

m == board.length
n = board[i].length
1 <= m, n <= 6
1 <= word.length <= 15
board and word consists of only lowercase and uppercase English letters.


Follow up: Could you use search pruning to make your solution faster with a larger board?
"""


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def backtrack(i, m, n, visited):
            nonlocal M, N
            directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            if i == len(word):
                return True

            if board[m][n] != word[i]:
                return False

            # When current element matches, backtrack to next direction

            found_word = False if i < len(word) - 1 else True
            # found_word = False
            for d in directions:
                next_m, next_n = m + d[0], n + d[1]
                if 0 <= next_m < M and 0 <= next_n < N and not visited[next_m][next_n]:
                    visited[m][n] = True
                    found_word = found_word or backtrack(i + 1, next_m, next_n, visited)
                    visited[m][n] = False

            return found_word

        M, N = len(board), len(board[0])

        res = False
        for m in range(M):
            for n in range(N):
                if board[m][n] == word[0]:
                    visited = [[False for n in range(N)] for m in range(M)]
                    res = res or backtrack(0, m, n, visited)

        return res