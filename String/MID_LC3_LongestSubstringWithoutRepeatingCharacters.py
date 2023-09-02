class Solution:
    # Given a string s, find the length of the longest substring without repeating characters.

    # def find_solution(self, str):
    #     # two pointers
    #     if len(str) <= 1:
    #         return len(str)
    #
    #     output = 1
    #     l, r = 0, 1
    #
    #     while r < len(str):
    #         cur_sub_str = str[l:r]
    #         # if it is non-repeating
    #         if str[r] not in cur_sub_str:
    #             cur_sub_str += str[r]
    #             r += 1
    #
    #         # if it is repeating
    #         else:
    #             output = max(output, len(cur_sub_str))
    #             l += 1
    #             r = l + 1
    #     output = max(output, len(cur_sub_str))
    #
    #     print(str, output)
    #     return output

    def find_solution(self, str):
        # hashmap
        if len(str) == 0:
            return 0
        occur_hash = {}
        start = 0
        output = 0

        # while i < len(str):
        for i in range(len(str)):
            if str[i] in occur_hash.keys():
                start = max(occur_hash[str[i]] + 1, start)
            occur_hash[str[i]] = i
            output = max(output, i - start + 1)
        return output

def main():
    s = Solution()

    result1 = s.find_solution("abcabcbb")
    result2 = s.find_solution("aab")
    result3 = s.find_solution("au")
    print(result1, result2, result3)


if __name__ == "__main__":
    main()