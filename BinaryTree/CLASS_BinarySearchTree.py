
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

    def remove(self, val, current=None, parent=None):
        if not current:
            current = self.root

        while current:
            if val < current.val:
                parent = current
                current = current.left
            elif val > current.val:
                parent = current
                current = current.right
            else:
                # Found the target node.
                # If node has left and right, find the min value from right and replace here
                # This branch works when the root node is the target value since it does not use the parent node
                if current.left and current.right:
                    next_min = self.find_extreme(current.right, is_max=False)
                    current.val = next_min
                    self.remove(val=next_min, current=current.right, parent=current)

                # If parent is None, which means target node is the root node
                elif not parent:
                    if current.left:
                        self.root = current.left
                    elif current.right:
                        self.root = current.right
                    else:
                        self.root = None

                # This branch and the one below do not work when parent is None, so we take care of it above
                elif current.left or current.right:
                    if parent.left == current:
                        parent.left = current.left if current.left else current.right
                    else:
                        parent.right = current.left if current.left else current.right

                elif not current.left and not current.right:
                    if parent.left == current:
                        parent.left = None
                    else:
                        parent.right = None

                self.size -= 1
                if self.print_outcome:
                    print(f"Removed {val} from the tree.")
                return


    def find_value(self, val):
        root = self.root

        while root:
            if val < root.val:
                root = root.left
            elif val > root.val:
                root = root.right
            else:
                print("Target value found")
                return root

        print("Target value not found")
        return None

    def construct(self, in_arr):
        for item in in_arr:
            self.insert(item)
        print("Constructed the tree.")

    def construct_balanced(self, in_arr):
        def helper(in_arr):
            if not in_arr:
                return
            l, r = 0, len(in_arr) - 1
            while l <= r:
                mid = (l + r) // 2
                self.insert(in_arr[mid])
                helper(in_arr[l:mid])
                helper((in_arr[mid+1:]))
                return
        helper(in_arr)
        if self.print_outcome:
            print("Constructed balanced BST.")


    # Return the maximum or the minimum node of the tree
    def find_extreme(self, root, is_max=True):
        if is_max:
            while root and root.right:
                root = root.right
        else:
            while root and root.left:
                root = root.left

        return root.val

    def print_by_level(self):
        if self.size == 0:
            return
        print("Printing tree...")
        root = self.root
        in_arr = [root]
        level = 0
        while len(in_arr) != 0:
            out_arr = [i.val for i in in_arr]
            print(f"Level {level}: {out_arr}")

            new_arr = []
            for node in in_arr:
                if node.left:
                    new_arr.append(node.left)
                if node.right:
                    new_arr.append(node.right)
            in_arr = new_arr.copy()
            level += 1

    def traverse_bfs(self):
        if not self.root:
            return

        re_arr = []
        root = self.root
        in_arr = [root]
        while len(in_arr) != 0:
            re_arr += [i.val for i in in_arr]
            new_arr = []
            for node in in_arr:
                if node.left:
                    new_arr.append(node.left)
                if node.right:
                    new_arr.append(node.right)
            in_arr = new_arr.copy()
        print(re_arr)
        return re_arr

    def traverse_dfs_inorder(self):
        def helper(root):
            if not root:
                return []
            while root:
                helper(root.left)
                out_arr.append(root.val)
                helper(root.right)
                return

        if not self.root:
            return []
        root = self.root
        out_arr = []
        helper(root)
        return out_arr

    def traverse_dfs_preorder(self):
        def helper(root):
            if not root:
                return []
            while root:
                out_arr.append(root.val)
                helper(root.left)
                helper(root.right)
                return

        if not self.root:
            return []
        root = self.root
        out_arr = []
        helper(root)
        return out_arr


    def traverse_dfs_postorder(self):
        def helper(root):
            if not root:
                return []
            while root:
                helper(root.left)
                helper(root.right)
                out_arr.append(root.val)
                return

        if not self.root:
            return []
        root = self.root
        out_arr = []
        helper(root)
        return out_arr

if __name__ == "__main__":
    tree = BinarySearchTree()

    l1 = [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29]
    tree.construct_balanced(l1)
    tree.print_by_level()
    # tree.remove(15)
    # tree.print_by_level()
    print(tree.traverse_dfs_inorder())
    print(tree.traverse_dfs_preorder())
    print(tree.traverse_dfs_postorder())

