"""
You have a graph of n nodes labeled from 0 to n - 1. You are given an integer n and a list of edges where
edges[i] = [ai, bi] indicates that there is an undirected edge between nodes ai and bi in the graph.

Return true if the edges of the given graph make up a valid tree, and false otherwise.



Example 1:


Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
Output: true
Example 2:


Input: n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
Output: false


Constraints:

1 <= n <= 2000
0 <= edges.length <= 5000
edges[i].length == 2
0 <= ai, bi < n
ai != bi
There are no self-loops or repeated edges.
"""


"""
To determine if a graph is a valid tree:
1. All nodes must be connected
2. Nodes cannot go in cycles(A -> B -> A trivial cycles don't count)
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
            return True
        else:
            return False

class Solution:
    def validTreeDFS(self, n: int, edges: List[List[int]]) -> bool:
        """
        In this approach, we first create a adjacent list, then use DFS to loop through each node and its neighbors
        - Maintain a parent variable to account for A->B->A cycles
        - Maintain a seen set for nodes already visited

        The graph is a tree is every node is visited, and there is no cycle
        """
        def dfs(node, parent):
            if node in seen:
                return
            seen.add(node)

            for n in adjacent[node]:
                if n == parent:
                    continue
                if n in seen:
                    return False
                res = dfs(n, node)
                if not res:
                    return False
            return True

        # Create adjacency list
        adjacent = [[] for i in range(n)]

        for e in edges:
            n1, n2 = e[0], e[1]
            adjacent[n1].append(n2)
            adjacent[n2].append(n1)

        # print(adjacent)

        seen = set()

        return dfs(0, -1) and len(seen) == n

    def validTreeIterativeDFS(self, n: int, edges: List[List[int]]) -> bool:
        """
        Additional observation: for a graph to be an valid tree, it must have exactly n-1 edges
        - If edge < n-1, some nodes are not connected
        - If edge > n-1, there must be cycles

        Therefore, on top of n-1 edge, we only need to make sure every node is visited by the DFS
        """

        if len(edges) != n-1:
            return False

        # Create adjacency list
        adjacent = [[] for i in range(n)]

        for e in edges:
            n1, n2 = e[0], e[1]
            adjacent[n1].append(n2)
            adjacent[n2].append(n1)

        seen = set()
        seen.add(0)
        stack = [0]

        while stack:
            node = stack.pop()
            for nei in adjacent[node]:
                if nei in seen:
                    continue
                seen.add(nei)
                stack.append(nei)

        return len(seen) == n

    def validTreeUnionFind(self, n: int, edges: List[List[int]]) -> bool:
        """
        Since we have the above observation, we could use Union Find to union all nodes. For any union operation,
        if we find out that the nodes are already connected, then it's a cycle and we could return False; if there has
        been no cycles and there are n-1 edges, then it's an valid tree.
        """
        if len(edges) != n-1:
            return False

        uf = UnionFind(n)
        for e in edges:
            n1, n2 = e[0], e[1]
            if not uf.union(n1, n2):
                return False
        return True


