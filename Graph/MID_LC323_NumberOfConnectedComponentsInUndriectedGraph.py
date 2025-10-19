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
        # Key is to add the return boolean here
        # This will tell us whether the given two nodes are already connected or not
            return True
        else:
            return False


class Solution:
    def countComponentsDFSIteration(self, n: int, edges: List[List[int]]) -> int:
        # Create adjacent list
        adjacent = [[] for i in range(n)]
        for n1, n2 in edges:
            adjacent[n1].append(n2)
            adjacent[n2].append(n1)

        print(adjacent)

        seen = set()
        res = 0
        # Start from node 0 to n-1, each time if the node is not seen before, increment res
        # For each node, use DFS to traverse to all neighbors and mark them as seen

        for start_node in range(n):
            if start_node not in seen:
                res += 1
                stack = [start_node]
                while stack:
                    node = stack.pop()
                    seen.add(node)
                    for nei in adjacent[node]:
                        if nei not in seen:
                            stack.append(nei)
        return res

    def countComponentsDFSRecursion(self, n: int, edges: List[List[int]]) -> int:
        # Create adjacent list
        adjacent = [[] for i in range(n)]
        for n1, n2 in edges:
            adjacent[n1].append(n2)
            adjacent[n2].append(n1)

        # print(adjacent)

        seen = set()
        res = 0

        def dfs(node):
            nonlocal seen, adjacent
            if node in seen:
                return
            else:
                seen.add(node)
                for nei in adjacent[node]:
                    dfs(nei)

        for start_node in range(n):
            if start_node not in seen:
                res += 1
                dfs(start_node)

        return res

    def countComponentsUnionFind(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        res = n

        for e in edges:
            e1, e2 = e
            if uf.union(e1, e2):
                res -= 1

        return res