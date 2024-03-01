"""
Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.



Example 1:

Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
Example 2:

Input: s = "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".


Constraints:

1 <= s.length <= 1000
s consists of lowercase English letters.
"""


class Solution:
    def countSubstringsBruteForce(self, s: str) -> int:
        """
        Find all combinations of substrings, check if one is palindrome

        Time: O(n^3) - nested for loop + compare string itself which is also O(n)
        """
        cnt = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                cur_sub = s[i:j+1]
                # The slicing syntax [::] takes three parameters: start, stop, and step. By specifying -1 as the step,
                # it iterates through the string in reverse order, effectively reversing it
                if cur_sub == cur_sub[::-1]:
                    cnt += 1
        return cnt

    def countSubstringsTwoPointersWrong(self, s: str) -> int:
        """
        WRONG APPROACH. But leaving here for future reflection.


        Consider 'abcba' and 'abccba'

        - Use 2 pointers both starting at beginning of the array
        - For s[left: right+1], or 'a': This is palindrome, and if the next one is itself(a), then it's also palindrome
        - Move right forward. 'ab': Not palindrome. If next is 'a' then it becomes one.
          If 'b' then it's palindrome when the next next is 'a'
        - Move right forward. 'abc': Not palindrome. If next is 'ba' then it becomes one.
          If 'c' then it's palindrome when the next next is 'ba'

        With the case above we can conclude:
        1. We need a string to store the remaining characters required for a palindrome, req
        2. Each iteration i, we include a new character and make comparisons
            a. If s[i] == req[0], remove the element from req since the palindrome requirement is partially met
               - If not req, then we have a palindrome
            b. If s[i] == s[i-1], it's NOT palindrome, and we don't add anything to the requirement
            c. If s[i] != req[0], it's NOT a palindrome, and we add s[i-1] to the front of the requirement
        """
        res = 1
        palin_hash = set(s[0])
        for i in range(1, len(s)):
            req = ""
            for j in range(i, len(s)):
                print(f"i: {i}, j: {j}")

                if i == j:
                    if not req and s[i:j+1] not in palin_hash:
                        res += 1
                        palin_hash.add(s[i:j+1])
                elif req and s[i] == req[0]:
                    req = req[1:]
                    if not req and s[i:j+1] not in palin_hash:
                        res += 1
                        palin_hash.add(s[i:j+1])
                elif s[i] == s[i-1]:
                    continue
                elif not req or s[j] != req[0]:
                    req = s[j - 1] + req

        return res

    def countSubstringsTwoPointers(self, s: str) -> int:
        """
        Why my initial thoughts are wrong? - Not considering the properties of the palindromes
        - Palindromes can expand from the center: if both sides are the same, then we have a bigger palindrome
        - Therefore, we shouldn't put left right pointers at the start of string and move towards the end
        - Instead, we should move it around the center of each element

        There are 2 scenarios:
        - If the length is odd, then we move outward and the boundary elements must be the same
        - If the length is even, then we move outward and the boundary elements, as well as the 2 middle elements
          must be the same
        """
        cnt = 0
        for i in range(len(s)):
            left, right = i, i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                cnt += 1
                left -= 1
                right += 1

        for i in range(len(s)):
            left, right = i, i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                cnt += 1
                left -= 1
                right += 1
        return cnt

    def countSubstringsTwoPointersRecursive(self, s: str) -> int:
        def find_palindrome(l, r):
            if l < 0 or r >= len(s) or s[l] != s[r]:
                return 0
            else:
                return 1 + find_palindrome(l-1, r+1)

        res = 0
        for i in range(len(s)):
            res += find_palindrome(i, i)
            res += find_palindrome(i, i+1)
        return res

s = Solution()
res = s.countSubstringsTwoPointersRecursive("abcba")
print(res)

res = s.countSubstringsTwoPointersRecursive("aaa")
print(res)