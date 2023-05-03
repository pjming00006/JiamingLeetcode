class Solution:

    def find_solution_tuple_hash(self, strs):
        sorted_strs = {}
        for s in strs:
            key = tuple(sorted(s))
            if key in sorted_strs:
                sorted_strs[key].append(s)
            else:
                sorted_strs[key] = [s]
        return sorted_strs.values()

    def find_solution_unicode_hash(self, strs):
        # No need for sorting
        hm = {}
        for s in strs:
            count = [0 for i in range(26)]
            for char in s:
                count[ord(char) - ord("a")] += 1
            hm[tuple(count)].append(s)
        return hm.values()

def main():
    s = Solution()

    result1 = s.find_solution_tuple_hash(["eat", "tea", "tan", "ate", "nat", "bat"])
    print(result1)

    result2 = s.find_solution_unicode_hash(["eat", "tea", "tan", "ate", "nat", "bat"])
    print(result2)

if __name__ == "__main__":
    main()