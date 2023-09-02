class Solution:

    def find_solution(self, strs):
        sorted_strs = []
        for str in strs:
            sorted_strs.append(''.join(sorted(str)))

        hm = {}
        for i, val in enumerate(sorted_strs):
            if val in hm:
                hm[val].append(i)
            else:
                hm[val] = [i]

        res = []
        for v in hm.values():
            sub_group = []
            for ind in v:
                sub_group.append(strs[ind])
            res.append(sub_group)
        return res

    def find_solution_tuple_hash(self, strs):
        sorted_strs = {}
        for s in strs:
            key = tuple(sorted(s))
            if key in sorted_strs:
                sorted_strs[key].append(s)
            else:
                sorted_strs[key] = [s]
        return sorted_strs.values()


def main():
    s = Solution()

    # result1 = s.find_solution(["eat","tea","tan","ate","nat","bat"])
    # print(result1)

    result2 = s.find_solution_tuple_hash(["eat", "tea", "tan", "ate", "nat", "bat"])
    print(result2)


if __name__ == "__main__":
    main()