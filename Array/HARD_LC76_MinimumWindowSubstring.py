"""
Given two strings s and t of lengths m and n respectively, return the minimum window
substring
 of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.



Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.


Constraints:

m == s.length
n == t.length
1 <= m, n <= 105
s and t consist of uppercase and lowercase English letters.


Follow up: Could you find an algorithm that runs in O(m + n) time?
"""


class Solution:
    def minWindowBruteForce(self, s: str, t: str) -> str:
        """
        Basic Observation:
        1. Since the substring must also account for duplicate, it is required that the substring of s is AT LEAST the
           length of t.
        2. Since we are finding the minimum window, the first and last character in the window must be within string t,
           otherwise it's not the optimal solution

        Idea:
        Input: s = "ADOBECODEBANC", t = "ABC"
        1. We start from the first element "A" since it has the character we are looking for
        2. Initialize a right pointer at "A" as well
        3. When the current substring is shorter than the target or does not contain all characters in target, we
           move the right pointer forward
           "ADO" -> "ADOB" -> "ADOBEC" Now the substring qualifies for the target, record the length
        4. Now we discard part of the substring until the second target character: "BEC", then start searching again
           "BEC" -> "BECODEB" -> "BECODEBA" Now record the new length if it's smaller than the previous one
        5. Keep going from "CODEBA"
        6. "BA" -> "BANC"
        """

        def if_valid(substring, t):
            for c in substring:
                if c in t:
                    ind = t.index(c)
                    t = t[:ind] + t[ind + 1:]
            if not t:
                return True
            else:
                return False

        left = -1
        target_len = len(t)
        ans = ""

        for i, char in enumerate(s):
            if char in t:
                left = i
                break
        if left < 0:
            return ""

        right = left
        while left < len(s) and right < len(s):
            if right - left + 1 < target_len:
                right += 1
            else:
                if if_valid(s[left: right+1], t):
                    if not ans or len(s[left: right+1]) < len(ans):
                        ans = s[left: right+1]
                    left += 1
                else:
                    right += 1

        return ans

    def minWindowTwoPointers(self, s: str, t: str) -> str:
        """
        Reflecting on the first solution, it's too computationally heavy to check if the current substring as a
        whole is a qualified one - we need some sort of mechanism to store information as we go

        We can use a hashmap to store the number of each element needed for target at the moment

        Algorithm:
        1. Initialize a hashmap, loop through target to store the number of occurrences for each element
        2. Use the hashmap to find the first qualifying substring and initialize left, right on boundary
        3. While left not reaching the end, we evaluate:
            - If current substring is the answer, we move left forward. As we move left, the left element drops
              out of the substring, so we need to know if this would affect the substring being qualified. If the left
              element is in the target, we increment the count in the hashmap to represent the need for that element.
              After the increment, if the needed count > 0, it means that the new substring is no longer qualified
              and we're missing the element at the left pointer
            - If current substring is NOT the answer, we move right forward. If the new right element is in the hashmap,
              we decrement the count. If the count of the missing value is now less than or equal to 0, then we find
              the element needed and the substring becomes a qualified one.
        """
        # Create a hash of the target string and the number of occurrences as values
        ans = ""
        ht = {}
        n = len(t)
        right = -1

        for c in t:
            if c not in ht.keys():
                ht[c] = 1
            else:
                ht[c] += 1

        # Use the hash table to find the first qualifying substring. If not, return ""
        for i, char in enumerate(s):
            if char in ht.keys():
                if ht[char] >= 1:
                    n -= 1
                ht[char] -= 1

            if n == 0:
                right = i
                break

        if right < 0:
            return ""

        left = 0
        is_ans = True
        next_missing = ""

        while left < len(s):
            if is_ans:
                if not ans or len(s[left:right+1]) < len(ans):
                    ans = s[left:right+1]
                if s[left] in ht.keys():
                    ht[s[left]] += 1
                    if ht[s[left]] > 0:
                        is_ans = False
                        next_missing = s[left]
                left += 1
            else:
                right += 1

                if right < len(s):
                    if s[right] in ht.keys():
                        ht[s[right]] -= 1
                        if ht[next_missing] <= 0:
                            is_ans = True
                else:
                    left += 1
        return ans

    def minWindowTwoPointersOptimized(self, s: str, t: str) -> str:
        """
        There is no need to use a separate logic to find the first qualifying substring. We can incorporate in the
        loop.
        """
        ht = {}

        for v in t:
            if v not in ht.keys():
                ht[v] = 1
            else:
                ht[v] += 1

        ans = ""
        n_missing = len(t)
        left, right = 0, -1

        while left < len(s):
            if n_missing > 0:
                right += 1
                if right < len(s):
                    if s[right] in ht.keys():
                        if ht[s[right]] > 0:
                            n_missing -= 1
                        ht[s[right]] -= 1
                else:
                    left += 1
            else:
                if not ans or len(s[left:right+1]) < len(ans):
                    ans = s[left:right+1]
                if s[left] in ht.keys():
                    ht[s[left]] += 1
                    if ht[s[left]] > 0:
                        n_missing += 1
                left += 1
        return ans


s = Solution()
res = s.minWindowTwoPointersOptimized("AOBECODEBANC", "ABC")
print(res)

res = s.minWindowTwoPointersOptimized("AB", "B")
print(res)

res = s.minWindowTwoPointersOptimized("BBA", "AB")
print(res)

