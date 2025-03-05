"""
Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”



Example 1:


Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.
Example 2:


Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.
Example 3:

Input: root = [2,1], p = 2, q = 1
Output: 2


Constraints:

The number of nodes in the tree is in the range [2, 105].
-109 <= Node.val <= 109
All Node.val are unique.
p != q
p and q will exist in the BST.
"""

class Solution:
    def lowestCommonAncestorRecursion(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        Refer to LC 236 for ordinary binary tree solution to lowest common ancestors

        We know that binary search tree is constructed in a way that, the left sub-tree contains nodes that are smaller
        or equal to the root, and the right sub-tree contains nodes that are greater than root. Therefore, there are
        3 scenarios:
        1. If both p and q are in the right sub-tree, then we need to search the right tree
        2. If both p and q are in the left sub-tree, then we need to search the left tree
        3. If both 1 and 2 are not true, then p and q must be on 2 sides of the current node, so the current node is
           the lowest common ancestor

        Time, Space: O(n)
        """
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        elif p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return root

    def lowestCommonAncestorIteration(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        Time: O(n)
        Space: O(1)
        """
        while root:
            if p.val > root.val and q.val > root.val:
                root = root.right
            elif p.val < root.val and q.val < root.val:
                root = root.left
            else:
                return root