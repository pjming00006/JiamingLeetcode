# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # post order dfs: left, right, root

        def dfs(node):
            if not node:
                return 0

            left_dep = dfs(node.left)
            right_dep = dfs(node.right)

            cur_dep = max(left_dep, right_dep) + 1

            return cur_dep

        return dfs(root)

    def maxDepthIteration(self, root: Optional[TreeNode]) -> int:
        # post order dfs: left, right, root
        stack = [(1, root)]
        res = 0

        if not root:
            return res

        while stack:
            cur_dep, node = stack.pop()
            res = max(res, cur_dep)
            if node.left:
                stack.append((cur_dep + 1, node.left))
            if node.right:
                stack.append((cur_dep + 1, node.right))
        return res