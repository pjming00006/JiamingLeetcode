from collections import deque

class Solution:
    def rightSideView(self, root):
        if not root:
            return []
        levels = []
        q = deque()
        q.append(root)

        level = 0
        while q:
            cur_len = len(q)
            for i in range(len(q)):
                cur_node = q.popleft()
                # If this is the last element in the level, append
                if i == cur_len - 1:
                    levels.append(cur_node.val)
                if cur_node.left: q.append(cur_node.left)
                if cur_node.right: q.append(cur_node.right)
            level += 1
        return levels

    def leftSideView(self, root):
        if not root:
            return []
        levels = []
        q = deque()
        q.append(root)

        level = 0
        while q:
            for i in range(len(q)):
                cur_node = q.popleft()
                # if this is the first element in the level, append
                if i == 0:
                    levels.append(cur_node.val)
                if cur_node.left: q.append(cur_node.left)
                if cur_node.right: q.append(cur_node.right)
            level += 1
        return levels