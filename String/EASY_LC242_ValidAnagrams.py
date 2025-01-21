class Solution:
    def isAnagramSort(self, s: str, t: str) -> bool:
        """
        Time: O(nlogn) since we utilize a sort
        Space: O(1)
        """
        s_sort = ''.join(sorted(s))
        t_sort = ''.join(sorted(t))
        return s_sort == t_sort

    def isAnagramHash(self, s: str, t: str) -> bool:
        """Time: O(n), Space: O(n)"""
        hm = {}

        for char in s:
            if char not in hm.keys():
                hm[char] = 1
            else:
                hm[char] += 1
        for char in t:
            if char not in hm.keys():
                return False
            hm[char] -= 1
            if hm[char] < 0:
                return False

        for v in hm.values():
            if v != 0:
                return False
        return True
