"""
A tree is an undirected graph in which any two vertices are connected by exactly one path. In other words, any connected graph without simple cycles is a tree.

Given a tree of n nodes labelled from 0 to n - 1, and an array of n - 1 edges where edges[i] = [ai, bi] indicates that there is an undirected edge between the two nodes ai and bi in the tree, you can choose any node of the tree as the root. When you select a node x as the root, the result tree has height h. Among all possible rooted trees, those with minimum height (i.e. min(h))  are called minimum height trees (MHTs).

Return a list of all MHTs' root labels. You can return the answer in any order.

The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.

 

Example 1:


Input: n = 4, edges = [[1,0],[1,2],[1,3]]
Output: [1]
Explanation: As shown, the height of the tree is 1 when the root is the node with label 1 which is the only MHT.
Example 2:


Input: n = 6, edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
Output: [3,4]
 

Constraints:

1 <= n <= 2 * 104
edges.length == n - 1
0 <= ai, bi < n
ai != bi
All the pairs (ai, bi) are distinct.
The given input is guaranteed to be a tree and there will be no repeated edges.
"""

"""
Key observations:
1. The problem states that there are no loops and 2 nodes can only have 1 edge. With the above 
definitions, we can rephrase the problem as finding out the nodes that are overall close to all 
other nodes, especially the leaf nodes.

2. For the tree-alike graph, the number of centroids is no more than 2. Because:
    - For even number of nodes, 2 centroids are possible
    - For odd number of nodes, only 1 is centroid

With those in mind, we can start trimming the graph from leaves(nodes with only 1 connection).
We delete the edge one by one, and add more leaves and delete their edges, until reaching the centroid,
or when remaining nodes <= 2

"""
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        from collections import defaultdict
        if n <= 2:
            return [i for i in range(n)]

        adj_list = defaultdict(set)
        for e in edges:
            start, end = e[0], e[1]
            adj_list[start].add(end)
            adj_list[end].add(start)
        
        leaves = []
        for k, v in adj_list.items():
            if len(v) == 1:
                leaves.append(k)

        # print(adj_list, leaves)

        remaining_node = n
        while remaining_node > 2:
            remaining_node -= len(leaves)
            new_leaves = []
            while leaves:
                cur_node = leaves.pop()
                cur_neighbors = adj_list[cur_node]
                for nei in cur_neighbors:
                    adj_list[nei].remove(cur_node)
                    if len(adj_list[nei]) == 1:
                        new_leaves.append(nei)
                del adj_list[cur_node]
            leaves = new_leaves

        # print(adj_list)
        return [k for k in adj_list.keys()]
