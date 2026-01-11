"""
Disjoint Set: An array, where the index represents the node value, and array value represents
the root node.

In a quick union disjoint set, the root node represents the immediate connection, not the final root;
In a quick find disjoint set, the root node is the final root
"""

# Root of node 0 is 1; root of node 1 is 1; root of node 2 is 2
disjoint_set = [1,1,2]

"""
Adjacency List: An array containing all nodes connected to the current node. Often implemented as a
hashmap, where key is current node, and value is an array of adjacent nodes
"""

adjacency_list = {
    "0": ["1"],
    "1": ["0"],
    "2": []
}