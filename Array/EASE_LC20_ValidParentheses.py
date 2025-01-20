"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.


Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false

Example 4:

Input: s = "([])"

Output: true



Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""

# Use stack. If it's an opening bracket, add to stack; if closing bracket, pop from stack and see if match.
# Return True only when stack becomes empty at end. Otherwise, return False
class Solution:
    def isValidStack(self, s: str) -> bool:
        mapping = {')': '(', '}':'{', ']':'['}
        stack = []
        for i in range(len(s)):
            if s[i] in ('(', '{', '['):
                stack.append(s[i])
            else:
                if not stack:
                    return False
                cur = stack.pop()
                if mapping[s[i]] != cur:
                    return False
        if not stack:
            return True
        return False

    def isValidStackCleared(self, s: str) -> bool:
        mapping = {')': '(', '}':'{', ']':'['}
        stack = []
        for c in s:
            if c not in mapping.keys():
                stack.append(c)
            else:
                if not stack:
                    return False
                cur = stack.pop()
                if mapping[c] != cur:
                    return False
        return not stack

