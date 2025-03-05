"""
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”



Example 1:


Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.
Example 2:


Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
Example 3:

Input: root = [1,2], p = 1, q = 2
Output: 1


Constraints:

The number of nodes in the tree is in the range [2, 105].
-109 <= Node.val <= 109
All Node.val are unique.
p != q
p and q will exist in the tree.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.ans = None

    def lowestCommonAncestorRecurssion(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        Traverse the tree, find p and q. When found, return true to parent. Recurse until 2 out of 3 nodes(current node,
        left, or right) are true.

        For each node:
        - If not does not exist, return False
        - If node is p or q, then mid is True
        - Traverse left and right to see if they contain p or q
        - If 2 out of 3 criteria(mid, left, right) are true, found the answer
        - If not, return

        Time, Space: O(n). Since we might need to tarverse the whole tree
        """
        def traverse_tree(cur_node):
            if not cur_node:
                return False

            if cur_node == p or cur_node == q:
                mid = True
            else:
                mid = False

            left = traverse_tree(cur_node.left)
            right = traverse_tree(cur_node.right)

            if mid + left + right >= 2:
                self.ans = cur_node

            return mid or left or right

        traverse_tree(root)
        return self.ans

    def lowestCommonAncestorIterationWithParentPointers(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        First, traverse tree to find p and q. When doing so, construct a hashmap of child-parent mappings.
        When both are found, construct a parent set using either p or q, then use the other to traverse the hashmap until
        parent is present in the list.

        Time: O(n)
        Space: O(n)
        """
        parents = {root: None}
        stack = [root]

        while p not in parents.keys() or q not in parents.keys():
            cur_node = stack.pop()

            if cur_node.left:
                parents[cur_node.left] = cur_node
                stack.append(cur_node.left)
            if cur_node.right:
                parents[cur_node.right] = cur_node
                stack.append(cur_node.right)

        p_parents = set()
        while p:
            p_parents.add(p)
            p = parents[p]

        while q not in p_parents:
            q = parents[q]
        return q

