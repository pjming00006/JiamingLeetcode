# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        stack = [root]
        res = []

        while stack:
            cur_node = stack.pop()
            res.append(cur_node.val)

            if cur_node.right:
                stack.append(cur_node.right)
            if cur_node.left:
                stack.append(cur_node.left)
        return res

    def preorderTraversalRecursion(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def traverse_tree(node):
            if not node:
                return

            res.append(node.val)
            traverse_tree(node.left)
            traverse_tree(node.right)

        traverse_tree(root)

        return res
