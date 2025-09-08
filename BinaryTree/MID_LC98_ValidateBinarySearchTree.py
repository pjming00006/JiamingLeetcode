"""
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys strictly less than the node's key.
The right subtree of a node contains only nodes with keys strictly greater than the node's key.
Both the left and right subtrees must also be binary search trees.


Example 1:


Input: root = [2,1,3]
Output: true
Example 2:


Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.


Constraints:

The number of nodes in the tree is in the range [1, 104].
-231 <= Node.val <= 231 - 1
"""
import math

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, low=-math.inf, high=math.inf):
            if not node:
                return True

            if node.val <= low or node.val >= high:
                return False

            return dfs(node.left, low, node.val) and dfs(node.right, node.val, high)

         return dfs(root)

    def isValidBSTIteration(self, root: Optional[TreeNode]) -> bool:
        stack = [(root, -math.inf, math.inf)]

        while stack:
            cur_node, low, high = stack.pop()
            if not cur_node:
                continue

            if cur_node.val <= low or cur_node.val >= high:
                return False

            stack.append((cur_node.left, low, cur_node.val))
            stack.append((cur_node.right, cur_node.val, high))
        return True

    def isValidBSTInorder(self, root: Optional[TreeNode]) -> bool:
        res = []

        def dfs(node):
            if not node:
                return

            dfs(node.left)
            res.append(node.val)
            dfs(node.right)

        dfs(root)
        for i in range(1, len(res)):
            if res[i] <= res[i - 1]:
                return False
        return True

    def isValidBSTInorderOptimized(self, root: Optional[TreeNode]) -> bool:
        last_val = -math.inf

        def dfs(node):
            nonlocal last_val
            if not node:
                return True

            if not dfs(node.left):
                return False

            if node.val <= last_val:
                return False
            else:
                last_val = node.val

            return dfs(node.right)

        return dfs(root)