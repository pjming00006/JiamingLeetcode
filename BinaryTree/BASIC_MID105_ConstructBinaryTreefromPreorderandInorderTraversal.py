# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        The intuition is that:
        1. Looping through the preorder array helps get the root of the current sub tree
        2. Knowing the root, then we could locate the root in the inorder array to divide the tree into left and right

        So to recursively work to the answer, we:
        1. For each element in preorder, create a node
        2. Find the element in inorder, divide the tree into left and right sub trees
        3. Recursively work in the sub trees
        """
        preorder_ind = 0
        inorder_hm = {}
        for i, n in enumerate(inorder):
            inorder_hm[n] = i

        def help_build_tree(left, right):
            nonlocal preorder_ind
            if left > right:
                return
            root_val = preorder[preorder_ind]
            cur_root = TreeNode(root_val)
            preorder_ind += 1

            cur_root.left = help_build_tree(left, inorder_hm[root_val] - 1)
            cur_root.right = help_build_tree(inorder_hm[root_val] + 1, right)

            return cur_root

        return help_build_tree(0, len(preorder) - 1)

    def buildTreeIteration(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        In the iteration approach, we don't have the recursion stack to help manage left sub-tree and right sub-tree
        We would need a stack to help determine if we should append current node to the left or right of the parent.

        Start from preorder, and manage a inorder index to track the end of the current left subtree.
        We create a node and compare the top of the stack with the node at inorder index. If they are not the same, it
        means that the left tree is not done yet, then we set parent.left to node and push node to the stack.

        If top of stack equals node at inorder index, it means the left sub tree is done, then we want to find the
        correct node to assign the right node. We keep popping from the stack and incrementing the inorder index until
        the top of the stack is not equal to the inorder index anymore. The node remains should be the parent node to
        assign the right child. Afterward, push the current node to the stack
        """
        pre_ind = 1
        in_ind = 0
        root = TreeNode(preorder[0])
        stack = [root]

        while pre_ind < len(preorder):
            root_val = preorder[pre_ind]
            pre_ind += 1
            cur_root = TreeNode(root_val)

            # If the left tree is done
            if stack and stack[-1].val == inorder[in_ind]:
                while stack and stack[-1].val == inorder[in_ind]:
                    parent = stack.pop()
                    in_ind += 1
                parent.right = cur_root

            # If the left tree is not done
            else:
                parent = stack[-1]
                parent.left = cur_root

            stack.append(cur_root)

        return root

