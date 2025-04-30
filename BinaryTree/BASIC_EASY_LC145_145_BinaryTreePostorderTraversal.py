# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = [(root, False)]
        res = []

        if not root:
            return res

        while stack:
            cur_node, visited = stack.pop()

            if not visited:
                stack.append((cur_node, True))
                if cur_node.right:
                    stack.append((cur_node.right, False))
                if cur_node.left:
                    stack.append((cur_node.left, False))
            else:
                res.append(cur_node.val)
        return res

    def postorderTraversalRecursion(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        if not root:
            return res

        def traverse_tree(node):
            if not node:
                return
            traverse_tree(node.left)
            traverse_tree(node.right)
            res.append(node.val)

        traverse_tree(root)
        return res