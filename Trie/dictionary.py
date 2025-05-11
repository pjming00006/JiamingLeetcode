from typing import List

class TreeNode:
    def __init__(self):
        self.xiaodeng = {}
        self.is_word = False

class Dictionary:
    def __init__(self):
        self.root = TreeNode()

    def insert_word(self, word: str):
        cur_node = self.root
        for char in word:
            if char not in cur_node.xiaodeng:
                cur_node.xiaodeng[char] = TreeNode()

            cur_node = cur_node.xiaodeng[char]
        cur_node.is_word = True

    # def delete_word(self, word:str):
    #     cur_node = self.root
    #     for char in word:
    #         if char not in cur_node.xiaodeng:
    #             return
    #         cur_node = cur_node.xiaodeng[char]
    #     cur_node.is_word = False
    #     # if a node has no children and the node is not a complete word, delete
    #     def dfs(node, word):
    #         if not word or (not node.is_word and not node.xiaodeng):
    #             return True
    #         remain_word = word[1:] if len(word) > 1 else None
    #         if remain_word:
    #             to_delete = dfs(node.xiaodeng[remain_word], remain_word)
    #         else:
    #             return
    #         if to_delete:
    #             node.xiaodeng.pop(char)
    #
    #         return not node.is_word and not node.xiaodeng

    def delete_word(self, word:str):
        def dfs(node, word, index):
            if index == len(word):
                # If the last node is not a completed word, then the word is never in the dictionary, so do nothing
                if node.is_word:
                    return False
                node.is_word = False
                return not node.xiaodeng

            char = word[index]
            next_node = node.xiaodeng[char]

            to_delete = dfs(next_node, word, index+1)
            if to_delete:
                node.xiaodeng.pop(word[index])

            return not node.is_word and not node.xiaodeng

    def prefix_search(self, prefix: str) -> List[str]:
        pass