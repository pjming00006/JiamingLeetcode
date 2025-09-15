"""
139. Word Break
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.



Example 1:

Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false


Constraints:

1 <= s.length <= 300
1 <= wordDict.length <= 1000
1 <= wordDict[i].length <= 20
s and wordDict[i] consist of only lowercase English letters.
All the strings of wordDict are unique
"""


class Solution:

    def wordBreakDFS(self, s: str, wordDict: List[str]) -> bool:
        from collections import deque

        q = deque()
        q.append(0)
        visited = set()

        while q:
            start = q.popleft()

            if start >= len(s):
                return True

            for end in range(start + 1, len(s) + 1):
                if s[start:end] in wordDict:
                    q.append(end)
                    visited.add(end)

        return False

    def wordBreakTopDown(self, s: str, wordDict: List[str]) -> bool:
        memo = [None for j in range(len(s))]
        wordDict = set(wordDict)

        def dp(i):
            nonlocal s, wordDict, memo
            if i == len(s):
                return True

            if memo[i] is not None:
                return memo[i]

            for word in wordDict:
                if s[i:i + len(word)] == word and dp(i + len(word)):
                    memo[i] = True
                    return memo[i]

            memo[i] = False
            return memo[i]

        dp(0)
        return memo[0]

    def wordBreakBottomUp(self, s: str, wordDict: List[str]) -> bool:
        memo = [False for j in range(len(s))]
        wordDict = set(wordDict)

        for i in range(len(s)):
            for word in wordDict:
                if i < len(word) - 1:
                    continue

                if i == len(word) - 1 or memo[i - len(word)]:
                    if s[i - len(word) + 1: i + 1] == word:
                        memo[i] = True
                        break

        return memo[-1]