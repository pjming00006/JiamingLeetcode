"""
Given a string s of '(' , ')' and lowercase English characters.

Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:

It is the empty string, contains only lowercase characters, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.


Example 1:

Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
Example 2:

Input: s = "a)b(c)d"
Output: "ab(c)d"
Example 3:

Input: s = "))(("
Output: ""
Explanation: An empty string is also valid.


Constraints:

1 <= s.length <= 105
s[i] is either '(' , ')', or lowercase English letter.
"""


class Solution:
    def minRemoveToMakeValidStack(self, s: str) -> str:
        """
        - If open paren, push to stack
        - If closing paren, check stack:
            - If stack has open, pop open, continue
            - If not, this close has to be removed
        - When loop is complete, if there is still open paren in the stack, they need to be removed
        """

        open_stack = []
        close_remove = []

        for i in range(len(s)):
            if s[i] == '(':
                open_stack.append(i)
            if s[i] == ')':
                if open_stack:
                    open_stack.pop()
                else:
                    close_remove.append(i)

        deletes = set(open_stack + close_remove)
        out = ""

        for i in range(len(s)):
            if i not in deletes:
                out += s[i]
        return out

    def minRemoveToMakeValidTwoPass(self, s: str) -> str:
        """
        - One key observation from previous approach is that, for close parenthesis, we can decide right away whether
          to keep it; but for open, we need to loop through the end
        - But, if we loop from the end, then for open, we can decide right away
        - Therefore, if we start from looping from the end to find opens to remove, then in the second pass, we construct
          the output while removing close, then we can do it in two passes
        """
        remove = []
        counterpart_cnt = 0

        for i in range(len(s)-1, -1, -1):
            if s[i] == ')':
                counterpart_cnt += 1
            elif s[i] == '(':
                if counterpart_cnt >= 1:
                    counterpart_cnt -= 1
                else:
                    remove.append(i)

        counterpart_cnt = 0
        out = ''
        """
        - For open parenthesis, we already know if they should be removed or not
        - For close parenthesis, it depends
        """
        for i in range(len(s)):
            if s[i] == '(':
                if i not in remove:
                    counterpart_cnt += 1
                    out += s[i]
            elif s[i] == ')':
                if counterpart_cnt >= 1:
                    counterpart_cnt -= 1
                    out += s[i]
            else:
                out += s[i]
        return out