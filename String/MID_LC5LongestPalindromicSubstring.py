"""
Given a string s, return the longest
palindromic

substring
 in s.



Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"


Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.
"""


class Solution:
    def longestPalindromeBruteForce(self, s: str) -> str:
        res = ""
        for i in range(len(s)):
            for j in range(i, len(s)):
                cur_sub = s[i:j+1]
                # The slicing syntax [::] takes three parameters: start, stop, and step. By specifying -1 as the step,
                # it iterates through the string in reverse order, effectively reversing it
                if cur_sub == cur_sub[::-1] and len(cur_sub) > len(res):
                    res = cur_sub
        return res


    def longestPalindromeTwoPointers(self, s: str) -> str:
        """
        Time: O(n^2). We iterate through the string twice and each time we potentially need to go over the whole string
        Space: O(1): Constant
        """
        res = ""
        for i in range(len(s)):
            left, right = i, i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > len(res):
                    res = s[left:right + 1]
                left -= 1
                right += 1

        for i in range(len(s)):
            left, right = i, i+1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > len(res):
                    res = s[left:right + 1]
                left -= 1
                right += 1
        return res



s = Solution()
res = s.longestPalindromeTwoPointers("babad")
print(res)

res = s.longestPalindromeTwoPointers("cbbd")
print(res)

res = s.longestPalindromeTwoPointers("aacabdkacaa")
print(res)
