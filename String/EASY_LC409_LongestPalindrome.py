"""
Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome.



Example 1:

Input: s = "abccccdd"
Output: 7
Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.
Example 2:

Input: s = "a"
Output: 1
Explanation: The longest palindrome that can be built is "a", whose length is 1.


Constraints:

1 <= s.length <= 2000
s consists of lowercase and/or uppercase English letters only.
"""

class Solution:
    def longestPalindrome(self, s: str) -> int:
        """
        Time: O(n)
        Space: O(1): The max number in the hashmap is 52
        """
        res = 0

        hm = {}
        for i in s:
            if i not in hm:
                hm[i] = 1
            else:
                hm[i] += 1

        has_odd = False

        for v in hm.values():
            if v % 2 == 0:
                res += v
            else:
                res += v - 1
                has_odd = True

        if has_odd:
            res += 1
        return res

    def longestPalindromeSet(self, s: str) -> int:
        """
        Time: O(n)
        Space: O(1): The max number in the hashmap is 52
        """
        res = 0

        matches = set()

        for i in s:
            if i not in matches:
                matches.add(i)
            else:
                matches.remove(i)
                res += 2
        if matches:
            res += 1
        return res