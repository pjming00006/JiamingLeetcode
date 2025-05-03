# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # postorder dfs: left, right, root
        res = -float("inf")

        def dfs(node):
            nonlocal res
            if not node:
                return 0

            left_val = max(dfs(node.left), 0)
            right_val = max(dfs(node.right), 0)

            max_path = left_val + right_val + node.val

            res = max(res, max_path)
mks9
            return max(left_val + node.val, right_val + node.val)

        dfs(root)
        return res

    def maxPathSumIteration(self, root: Optional[TreeNode]) -> int:
        """
        Use a dictionary to track each node's contribution to sum
        """
        # postorder dfs: left, right, root
        res = -float("inf")

        stack = [(root, False)]

        node_max_path = {}

        while stack:
            node, visited = stack.pop()

            if not visited:
                stack.append((node, True))
                if node.right:
                    stack.append((node.right, False))
                if node.left:
                    stack.append((node.left, False))
            else:
                left_val = max(node_max_path.get(node.left, 0), 0)
                right_val = max(node_max_path.get(node.right, 0), 0)

                max_path = left_val + right_val + node.val

                res = max(res, max_path)
                node_max_path[node] = max(left_val + node.val, right_val + node.val)
        return res
