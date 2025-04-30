# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        from collections import deque

        q = deque()
        q.append([root])
        res = []
        if not root:
            return res

        while q:
            cur_q = q.popleft()
            cur_res = []
            next_q = []
            for node in cur_q:
                cur_res.append(node.val)
                if node.left:
                    next_q.append(node.left)
                if node.right:
                    next_q.append(node.right)
            if cur_res:
                res.append(cur_res)
            if next_q:
                q.append(next_q)
        return res




