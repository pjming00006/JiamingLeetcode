"""
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.



Example 1:

Input: n = 5, bad = 4
Output: 4
Explanation:
call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true
Then 4 is the first bad version.
Example 2:

Input: n = 1, bad = 1
Output: 1


Constraints:

1 <= bad <= n <= 231 - 1
"""

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

def isBadVersion(version_num):
    if version_num in [4, 5]:
        return True
    else:
        return False

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, r = 1, n
        min_bad = n

        while l < r:
            """
            The trick of this question is that if we use (l + r) // 2, the function runs into an infinite loop. This
            is because we are not finding 'an answer' but finding the earliest occurrence of an answer. For instance, if
            left = 3 and right = 4 then the function will keep going forever.
            
            Using mid = l + ((r - l) // 2) avoids this problem, because when left = 3 and right = 4 the ((r - l) // 2)
            part will reduce to zero
            """
            mid = l + ((r - l) // 2)
            cur_bad = isBadVersion(mid)
            if cur_bad:
                min_bad = min(min_bad, mid)
                # If mid is bad then the earliest of all might be mid or somewhere before mid, so we still include mid
                r = mid
            else:
                # If mid is not bad then the only possibility of finding the bad is the right half
                l = mid + 1
        return min_bad

