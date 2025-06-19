"""
Given the root of a binary tree, return the vertical order traversal of its nodes' values. (i.e., from top to bottom, column by column).

If two nodes are in the same row and column, the order should be from left to right.



Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[9],[3,15],[20],[7]]
Example 2:


Input: root = [3,9,8,4,0,1,7]
Output: [[4],[9],[3,0,1],[8],[7]]
Example 3:


Input: root = [1,2,3,4,10,9,11,null,5,null,null,null,null,null,null,null,6]
Output: [[4],[2,5],[1,10,9,6],[3],[11]]


Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Level order is mid, left, right, and we only need to figure out what column each node is in and group by it
        Therefore, we can maintain a hashmap where key is column number and value is a list of nodes. Note that since
        we use level order traversal, the list is already sorted in the order we want
        """
        # level order
        if not root:
            return []
        from collections import deque
        q = deque([(root, 0)])
        hm = {}

        while q:
            cur_node, col = q.popleft()
            hm[col] = hm.get(col, []) + [cur_node.val]
            if cur_node.left:
                q.append((cur_node.left, col - 1))
            if cur_node.right:
                q.append((cur_node.right, col + 1))

        sorted_hm = sorted([(k, v) for k, v in hm.items()], key=lambda x: x[0])
        return [i[1] for i in sorted_hm]

    def verticalOrderNoSorting(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        In the previous approach, we still need sorting and that increases the time complexity to O(NlogN).
        We can avoid it by maintaining a min and max column index and loop through the index
        """
        # level order
        if not root:
            return []
        from collections import deque
        q = deque([(root, 0)])
        min_col, max_col = 0, 0
        hm = {}

        while q:
            cur_node, col = q.popleft()
            min_col = min(col, min_col)
            max_col = max(col, max_col)
            hm[col] = hm.get(col, []) + [cur_node.val]
            if cur_node.left:
                q.append((cur_node.left, col - 1))
            if cur_node.right:
                q.append((cur_node.right, col + 1))

        return [hm[i] for i in range(min_col, max_col + 1)]
