"""
Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.



Example 1:

Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".


Constraints:

1 <= s.length, p.length <= 3 * 104
s and p consist of lowercase English letters.
"""


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        if len(p) > len(s):
            return res

        p_hm = {}
        for c in p:
            if c in p_hm:
                p_hm[c] += 1
            else:
                p_hm[c] = 1

        s_hm = {}
        left, right = 0, 0

        while right < len(s):
            # print(left, right, s[left:right+1])
            c = s[right]
            if c not in s_hm:
                s_hm[c] = 1
            else:
                s_hm[c] += 1

            # print(s_hm)
            if s_hm == p_hm:
                res.append(left)

            if right + 1 - len(p) == left:
                # print("now a full string")
                if s_hm[s[left]] == 1:
                    del s_hm[s[left]]
                else:
                    s_hm[s[left]] -= 1
                left += 1

            right += 1
        return res