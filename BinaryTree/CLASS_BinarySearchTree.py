
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self, print_outcome=False):
        self.size = 0
        self.root = None
        self.print_outcome = print_outcome

    def insert(self, val):
        # If tree is empty, insert at root
        new_node = TreeNode(val)
        if self.size == 0:
            self.root = new_node
            self.size += 1
            if self.print_outcome:
                print(f"Inserted {val} at root.")
        else:
            root = self.root
            # If val is smaller than current node, traverse to the left; otherwise to the right
            while True:
                if val < root.val:
                    if not root.left:
                        root.left = new_node
                        if self.print_outcome:
                            print(f"Inserted {val} at leaf.")
                        return
                    else:
                        root = root.left
                elif val >= root.val:
                    if not root.right:
                        root.right = new_node
                        if self.print_outcome:
                            print(f"Inserted {val} at leaf.")
                        return
                    else:
                        root = root.right



    def remove(self, val):
        # 3 scenarios: node at leaf, node has 1 child, node has 2 children

        parent = self.root
        target_node = self.find_value(val)

        if target_node:
            while True:
                if parent == target_node:
                    print("111")
                else:
                    if val < parent.val:
                        if parent.left == target_node:
                            print("Found!")
                            is_left = True
                            break
                        else:
                            parent = parent.left
                    else:
                        if parent.right == target_node:
                            print("Found!")
                            is_left = False
                            break
                        else:
                            parent = parent.right
            # Type 1: node is leaf
            if not target_node.left and not target_node.right:
                if is_left:
                    parent.left = None
                else:
                    parent.right = None

            # Type 2: node has 1 child


    def find_value(self, val):
        root = self.root

        while root:
            if root.val == val:
                print("Found the target value.")
                return root
            else:
                if val < root.val:
                    root = root.left
                else:
                    root = root.right

        print("Target value not found")
        return None

    def construct(self, in_arr):
        for item in in_arr:
            self.insert(item)
        print("Constructed the tree.")

    # Return the maximum or the minimum node of the tree
    def find_extreme(self, root, is_max=True):
        if is_max:
            while root and root.right:
                root = root.right
        else:
            while root and root.left:
                root = root.left

        return root

    def print_by_level(self):
        if self.size == 0:
            return

        root = self.root
        in_arr = [root]
        while len(in_arr) != 0:
            out_arr = [i.val for i in in_arr]
            print(out_arr)
            new_arr = []
            for node in in_arr:
                if node.left:
                    new_arr.append(node.left)
                if node.right:
                    new_arr.append(node.right)
            in_arr = new_arr.copy()


if __name__ == "__main__":
    tree = BinarySearchTree()

    tree.construct([10, 5, 15, 3, 7, 12, 17])
    tree.print_by_level()

