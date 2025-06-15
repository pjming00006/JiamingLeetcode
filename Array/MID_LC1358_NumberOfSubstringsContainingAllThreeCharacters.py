class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        """
        Sliding Window:
        - Keep a two pointer sliding window and a hashmap storing the frequency of each character
        - While right is not reaching the end, add the character at right to the frequency map and increment right
        - If a valid substring is found, that means the substring itself and all substrings achieved by incrementing
          right are valid substrings, so increment count by len(s) - right. Once done, we should move left forward,
          until the substring is no longer valid
        - Once no longer valid, move right forward

        Time, Space: O(n), O(1)
        """
        hm = {}

        left, right, cnt = 0, 0, 0

        while right < len(s):
            hm[s[right]] = hm.get(s[right], 0) + 1

            while hm.get('a', 0) >= 1 and hm.get('b', 0) and hm.get('c', 0) >= 1:
                cnt += len(s) - right
                hm[s[left]] -= 1
                left += 1

            right += 1
        return cnt

    def numberOfSubstringsLastPosition(self, s: str) -> int:
        """
        Last Position Tracking:
        - We keep a hm that represent the last seen index for each character. If not yet seen, the index is -1
        - Iterate through the string and update the last seen index
        - When all three characters are found, we want to know what's the minimum index among the 3
        - Increment count by min index + 1, this is to count all valid substrings that we can get so far

        Time, Space: O(n), O(1)
        """
        hm = {'a': -1, 'b': -1, 'c': -1}
        cnt = 0

        for i in range(len(s)):
            char = s[i]
            hm[char] = i

            if hm['a'] >= 0 and hm['b'] >= 0 and hm['c'] >= 0:
                min_index = min(hm['a'], hm['b'], hm['c'])
                cnt += min_index + 1
        return cnt