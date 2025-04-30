# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        # Use postorder: left, right, root
        max_path = 0

        def dfs(node):
            nonlocal max_path
            if not node:
                return 0

            left_len = dfs(node.left)
            right_len = dfs(node.right)

            if node.left and node.left.val == node.val:
                left_len += 1
            else:
                left_len = 0
            if node.right and node.right.val == node.val:
                right_len += 1
            else:
                right_len = 0

            cur_len = left_len + right_len
            max_path = max(cur_len, max_path)

            return max(left_len, right_len)

        dfs(root)
        return max_path

    def longestUnivaluePathIteration(self, root: Optional[TreeNode]) -> int:
        # Use postorder dfs: left, right, root

        stack = [(root, False)]
        max_path = 0
        node_left_right_lens = {}

        while stack:
            cur_node, visited = stack.pop()

            if not cur_node:
                continue

            if not visited:
                stack.append((cur_node, True))
                stack.append((cur_node.right, False))
                stack.append((cur_node.left, False))
            else:
                cur_left, cur_right = 0, 0
                if cur_node.left and cur_node.left.val == cur_node.val:
                    left_len, right_len = node_left_right_lens.get(cur_node.left, (0, 0))
                    cur_left = max(left_len, right_len) + 1
                if cur_node.right and cur_node.right.val == cur_node.val:
                    left_len, right_len = node_left_right_lens.get(cur_node.right, (0, 0))
                    cur_right = max(left_len, right_len) + 1

                cur_len = cur_left + cur_right
                max_path = max(max_path, cur_len)
                node_left_right_lens[cur_node] = (cur_left, cur_right)

        return max_path




