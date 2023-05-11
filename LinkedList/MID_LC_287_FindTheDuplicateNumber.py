class Solution:
    def findDuplicate(self, nums):
        slow = nums[0]
        for i, v in enumerate(nums):
            nxt = nums[i]
            nxt_nxt = nums[nxt]



nums = [1,4,3,2,3]
index = [0,1,2,3,4]