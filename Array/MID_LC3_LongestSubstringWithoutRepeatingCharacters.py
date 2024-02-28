"""
Given a string s, find the length of the longest
substring
 without repeating characters.



Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""


class Solution:
    def lengthOfLongestSubstringBruteForce(self, s: str) -> int:
        """
        Brute force: nested for loops
        - For each element, grab all possible substring starting with this element
        - Record the longest substring
        """
        if len(s) == 1 or len(s) == 0:
            return len(s)

        ans = 1
        for i in range(len(s) - 1):
            cur_substring = s[i]
            cur_max = 1
            for j in range(i+1, len(s)):
                if s[j] not in cur_substring:
                    cur_substring += s[j]
                    cur_max += 1
                    ans = max(cur_max, ans)
                else:
                    break
        return ans

    def lengthOfLongestSubstringSlidingWindow(self, s: str) -> int:
        """
        - Initialize left, right at index 0, 1
        - While not to the end, move right pointer forward
        - Check if right element exists in the substring
        - If not, add to substring and update sum
        - If exists, move left forward
        """
        if len(s) == 0 or len(s) == 1:
            return len(s)

        cur_max, ans, left, right = 1, 1, 0, 1
        while right < len(s):
            cur_substring = s[left: right]
            if s[right] not in cur_substring:
                cur_substring += s[right]
                cur_max += 1
                right += 1
            else:
                ans = max(ans, cur_max)
                left += 1
                cur_max -= 1

        ans = max(ans, cur_max)
        return ans

    def lengthOfLongestSubstringSet(self, s: str) -> int:
        """
        Searching through a string to find an element is time inefficient, so we can use a set to track
        the history of elements
        """
        if len(s) == 0 or len(s) == 1:
            return len(s)

        ans, left, right = 1, 0, 1
        ht = set(s[0])
        while right < len(s):
            if s[right] not in ht:
                ht.add(s[right])
                right += 1
            else:
                ans = max(ans, len(ht))
                ht.remove(s[left])
                left += 1

        ans = max(ans, len(ht))
        return ans

    def lengthOfLongestSubstringTimeOptimized(self, s: str) -> int:
        """
        When we have a dupe, we always move left forward by 1. But if the dupe is the last element of current
        substring, then it takes several iterations to get there. If we store the indexes of each element we can
        traverse faster when having dupes.

        Trick here is that we need to additionally evaluate ht[s[right]] < left. If the stored index is smaller
        than left then we ignore them and continue to update the substring
        """
        if len(s) == 0 or len(s) == 1:
            return len(s)

        ans, left, right = 1, 0, 1
        ht = {s[0]: 0}
        while right < len(s):
            if s[right] not in ht.keys() or ht[s[right]] < left:
                ans = max(ans, right - left + 1)
                ht[s[right]] = right
                right += 1
            else:
                left = ht[s[right]] + 1
                ht[s[right]] = right
                right += 1
            # print(f"left: {left}, right: {right}, ans: {ans}, ht: {ht}")

        return ans


s = Solution()
res = s.lengthOfLongestSubstringTimeOptimized("abcabcbb")
print(res)

res = s.lengthOfLongestSubstringTimeOptimized("bbbbb")
print(res)

res = s.lengthOfLongestSubstringTimeOptimized("pwwkew")
print(res)

res = s.lengthOfLongestSubstringTimeOptimized("au")
print(res)

res = s.lengthOfLongestSubstringTimeOptimized("dvdf")
print(res)

res = s.lengthOfLongestSubstringTimeOptimized("tmmzuxt")
print(res)

