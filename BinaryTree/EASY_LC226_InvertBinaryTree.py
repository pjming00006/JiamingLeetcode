"""
Given the root of a binary tree, invert the tree, and return its root.

Example 1:

Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]
Example 2:


Input: root = [2,1,3]
Output: [2,3,1]
Example 3:

Input: root = []
Output: []


Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
"""
from CLASS_BinarySearchTree import TreeNode


class Solution:
    def invertTreeRecurssion(self, root: TreeNode) -> TreeNode:
        """
        Time: O(n), Space: O(n). Space can be interpreted as O(h), where h is the height of the tree.
        If the tree is deep then the recursive stack is big. But since h < n we can call it O(n)
        """
        if not root:
            return root

        new_left = self.invertTree(root.right)
        new_right = self.invertTree(root.left)

        root.left = new_left
        root.right = new_right
        return root

    def invertTreeIteration(self, root: TreeNode) -> TreeNode:
        """
        Time: O(n), Space: O(n)
        """
        q = [root]
        while root and q:
            cur_node = q.pop()
            if cur_node.left:
                q.append(cur_node.left)
            if cur_node.right:
                q.append(cur_node.right)
            cur_node.left, cur_node.right = cur_node.right, cur_node.left
        return root