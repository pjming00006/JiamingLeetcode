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
    def smallestStringWithSwapsUnionFind(self, s: str, pairs: List[List[int]]) -> str:
        """
        1. For each connected component, store all string indices and characters in hashmap
        2. Create dummy output string with same length
        3. Loop through the hashmap, sort indices and characters ascendingly
        4. Assign the sorted characters to the sorted indices
        """

        # Connect all pairs
        uf = UnionFind(len(s))
        for i1, i2 in pairs:
            uf.union(i1, i2)

        # Find the ultimate root for each node. This is required,
        # since uf.root might not store the ultimate root for each node until uf.find() is run
        for i in range(len(s)):
            uf.find(i)

        # Construct a hm to store root as key, indexes and characters as values
        hm = {}
        for index, root in enumerate(uf.root):
            char = s[index]
            if root not in hm.keys():
                hm[root] = ([char], [index])
            else:
                hm[root][0].append(char)
                hm[root][1].append(index)

        # For each group, re-assign char to index by sorting
        res = [0] * len(s)
        for root in hm.keys():
            chars, indices = hm[root]
            chars.sort()
            indices.sort()

            for i in range(len(chars)):
                res[indices[i]] = chars[i]

        return ''.join(res)

    def smallestStringWithSwapsDFS(self, s: str, pairs: List[List[int]]) -> str:
        """
        Same idea, using an adjacent list
        """

        # Construct Adjacent List
        adjacent = [[] for i in range(len(s))]

        for i1, i2 in pairs:
            adjacent[i1].append(i2)
            adjacent[i2].append(i1)

        seen = set()
        connected_components = []
        for start_index in range(len(s)):
            if start_index not in seen:
                seen.add(start_index)
                stack = [start_index]
                indices = []
                chars = []

                while stack:
                    cur_index = stack.pop()
                    indices.append(cur_index)
                    chars.append(s[cur_index])
                    for nei in adjacent[cur_index]:
                        if nei not in seen:
                            seen.add(nei)
                            stack.append(nei)

                connected_components.append((indices, chars))

        res = [""] * len(s)

        for indices, chars in connected_components:
            indices.sort()
            chars.sort()

            for i in range(len(indices)):
                res[indices[i]] = chars[i]

        return "".join(res)

