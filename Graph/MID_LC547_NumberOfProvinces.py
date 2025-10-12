"""
There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.



Example 1:


Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2
Example 2:


Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3


Constraints:

1 <= n <= 200
n == isConnected.length
n == isConnected[i].length
isConnected[i][j] is 1 or 0.
isConnected[i][i] == 1
isConnected[i][j] == isConnected[j][i]
"""


class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1 for i in range(size)]

    # Returns the root of the node
    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    # Returns if 2 nodes are connected
    def connected(self, x, y):
        return self.find(x) == self.find(y)

    def union(self, x, y):
        rootX, rootY = self.find(x), self.find(y)

        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootY] > self.rank[rootX]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1


class Solution:
    def findCircleNumUnionFind(self, isConnected: List[List[int]]) -> int:
        """
        Approach 1: Treat it as a graph and apply union find
        - For each node with another node, if they are connected, union them
        - Maintain a count of nodes, each time with union, decrement 1
        - Return the final count

        """
        n = len(isConnected)
        uf = UnionFind(n)

        cnt = n

        for i in range(len(isConnected)):
            for j in range(i + 1, len(isConnected[0])):
                if isConnected[i][j] == 1 and uf.find(i) != uf.find(j):
                    cnt -= 1
                    uf.union(i, j)

        return cnt

    def findCircleNumDFS(self, isConnected: List[List[int]]) -> int:

        def dfs(node, isConnected):
            nonlocal visited
            visited[node] = True
            for j in range(len(isConnected[node])):
                if isConnected[node][j] == 1 and not visited[j]:
                    dfs(j, isConnected)

        visited = [False for i in range(len(isConnected))]
        cnt = 0

        for i in range(len(isConnected)):
            if not visited[i]:
                cnt += 1
                dfs(i, isConnected)

        return cnt

    def findCircleNumBFS(self, isConnected: List[List[int]]) -> int:
        from collections import deque
        visited = [False for i in range(len(isConnected))]
        cnt = 0

        for i in range(len(isConnected)):
            if not visited[i]:
                cnt += 1
                q = deque()
                q.append(i)

                while q:
                    node = q.popleft()
                    visited[node] = True
                    conn = isConnected[node]
                    for j in range(len(conn)):
                        if conn[j] == 1 and not visited[j]:
                            q.append(j)

        return cnt
