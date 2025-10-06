input_graph = [(0,1), (0,2), (1,3), (4,8), (5,6), (5,7)]
check_connected = [(0,3), (1,5), (7,8)]

"""
For disjoint sets, we want to use an array, where the index represents the node, and the value represents the node
that the current node connects to.

In a 'quick find' algorithm, we want to make finding root node the quickest. For that, we could always have the array
value to store the root node.
"""
class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]

    # Returns the root of the node
    def find(self, x):
        return self.root[x]

    # Returns if 2 nodes are connected
    def connected(self, x, y):
        return self.find(x) == self.find(y)

    def union(self, x, y):
        rootX, rootY = self.find(x), self.find(y)

        if rootX != rootY:
            for i in range(len(self.root)):
                if self.root[i] == rootY:
                    self.root[i] = rootX


ds = UnionFind(10)
for nodes in input_graph:
    x, y = nodes
    ds.union(x, y)
print(ds.root)

for nodes in check_connected:
    x, y = nodes
    res = ds.connected(x, y)
    print(x, y, res)


