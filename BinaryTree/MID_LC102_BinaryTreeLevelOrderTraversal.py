from CLASS_BinarySearchTree import BinarySearchTree, TreeNode
from Queue.CLASS_QueueLinkedList import QueueLinkedList
from collections import deque


class BinaryTree(BinarySearchTree):
    def __init__(self):
        BinarySearchTree.__init__(self)

    def insert(self, in_arr: QueueLinkedList):
        if in_arr.size == 0:
            return []

        first_node = TreeNode(in_arr.dequeue())
        self.root = first_node
        self.size += 1

        node_queue = QueueLinkedList()
        node_queue.enqueue(first_node)
        node_queue.print_queue()

        while node_queue and in_arr.size != 0:
            cur_node = node_queue.dequeue()
            next_val = in_arr.dequeue()
            print(f"next val: {next_val}")
            if next_val:
                cur_node.left = TreeNode(next_val)
                self.size += 1
            next_val = in_arr.dequeue()
            print(f"next val: {next_val}")
            if next_val:
                cur_node.right = TreeNode(next_val)
                self.size += 1

            if cur_node.left:
                node_queue.enqueue(cur_node.left)
            if cur_node.right:
                node_queue.enqueue(cur_node.right)

    def levelOrder_lc_solution(self, root):
        if not root:
            return []

        out_arr = []
        q = deque()
        q.append(root)

        while True:
            res = []
            new_q = deque()
            while q:
                cur_node = q.popleft()
                res.append(cur_node.val)
                if cur_node.left:
                    new_q.append(cur_node.left)
                if cur_node.right:
                    new_q.append(cur_node.right)

            out_arr.append(res)

            if not new_q:
                break
            q = new_q.copy()
        return out_arr


if __name__ == "__main__":
    tree = BinaryTree()
    q = QueueLinkedList()
    l1 = [1,2,3,None,4,5]
    for i in l1:
        q.enqueue(i)
    q.print_queue()

    tree.insert(q)
    tree.print_by_level()