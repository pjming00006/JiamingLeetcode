# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = [(root, False)]
        res = []

        if not root:
            return res

        while stack:
            cur_node, visited = stack.pop()
            if not visited:
                if cur_node.right:
                    stack.append((cur_node.right, False))
                stack.append((cur_node, True))
                if cur_node.left:
                    stack.append((cur_node.left, False))
            else:
                res.append(cur_node.val)

        return res

    def inorderTraversalRecursion(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return []

        def traverse_tree(node):
            if not node:
                return

            traverse_tree(node.left)
            res.append(node.val)
            traverse_tree(node.right)

        traverse_tree(root)
        return res


