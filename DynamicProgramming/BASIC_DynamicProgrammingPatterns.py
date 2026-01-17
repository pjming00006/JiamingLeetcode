# 2 primary types: top-down and bottom-up

"""
Top down: usually invovles a backtrack algorithm: try option A, find result; backtrack, try option B,
find result, compare the 2.

- Need to find correct stopping condition
- Need to perform backtrack to prevent double-counting
- Optimal solution needs memorization

Memorization patterns:
Usually, we have a funciton backtrack(i). We can either:
- Add @cache on top of the function, or
- Initialize memo = [0] * len(input). Then update memo[i]
"""