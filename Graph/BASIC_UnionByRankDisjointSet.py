input_graph = [(0,1), (0,2), (1,3), (4,8), (5,6), (5,7)]
check_connected = [(0,3), (1,5), (7,8)]

"""
This is the optimization on the quick union algorithm. In quick union, we arbitrarily use either one of the 2 roots as
the new root; this can be inefficient. In union by rank algorithm, we maintain a 'rank' array to store the current 
height, and always use the root with higher height as the root.
"""
class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1 for i in range(size)]

    # Returns the root of the node
    def find(self, x):
        while self.root[x] != x:
            x = self.root[x]
        return x

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


ds = UnionFind(10)
for nodes in input_graph:
    x, y = nodes
    ds.union(x, y)
print(ds.root)

for nodes in check_connected:
    x, y = nodes
    res = ds.connected(x, y)
    print(x, y, res)


