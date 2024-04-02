"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.



Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]


Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
"""

class Solution:
    """
    Key idea: sort the strings before processing significantly simplify the problem.

    Time: suppose average length of string is k. Sorting costs O(klogk)
          We iterate the input twice so O(n)
          Overall, O(nklogk)
    Space:
    Storage for Sorted Strings: O(nk), as you store each sorted string.
    HashMap: O(n) for storing indices. Note that the space taken by the keys is included in the calculation for storing sorted strings.
    Result List: Up to O(nk), since you're essentially reorganizing the input strings.
    So, the total space complexity is
s
    O(nk), accounting for the storage of the input and the additional data structures used.
    """
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


    def find_solution_one_pass(self, strs):
        sorted_strs = {}
        for s in strs:
            key = "".join(sorted(s))
            if key in sorted_strs.keys():
                sorted_strs[key].append(s)
            else:
                sorted_strs[key] = [s]
        return list(sorted_strs.values())


def main():
    s = Solution()

    res = s.find_solution(["eat","tea","tan","ate","nat","bat"])
    print(res)

    res = s.find_solution_one_pass(["eat", "tea", "tan", "ate", "nat", "bat"])
    print(res)


if __name__ == "__main__":
    main()