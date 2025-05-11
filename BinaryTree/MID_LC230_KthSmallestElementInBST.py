"""
Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.



Example 1:


Input: root = [3,1,4,null,2], k = 1
Output: 1
Example 2:


Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3


Constraints:

The number of nodes in the tree is n.
1 <= k <= n <= 104
0 <= Node.val <= 104
"""

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # BST: everything smaller than root is on the left, everything greater than root is on the right
        # Use in-order: left, root, right

        stack = [(root, False)]
        cnt = 1
        while stack:
            node, visited = stack.pop()

            if not visited:
                if node.right:
                    stack.append((node.right, False))
                stack.append((node, True))
                if node.left:
                    stack.append((node.left, False))
            else:
                if cnt == k:
                    return node.val
                else:
                    cnt += 1

    def kthSmallestRecursion(self, root: Optional[TreeNode], k: int) -> int:
        # BST: everything smaller than root is on the left, everything greater than root is on the right
        # Use in-order: left, root, right
        res = None

        def dfs(node):
            nonlocal k, res
            if not node:
                return
            dfs(node.left)

            k -= 1
            if k == 0:
                res = node.val
                return

            dfs(node.right)

        dfs(root)

        return res