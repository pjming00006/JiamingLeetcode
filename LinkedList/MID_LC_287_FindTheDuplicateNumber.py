class Solution:
    def findDuplicate(self, nums):
        # This approach treats the array as linked list and utilize the way to find cycle in a linked list
        slow, fast = 0, 0

        while nums[fast] and nums[nums[fast]]:
            slow = nums[slow]
            fast = nums[nums[fast]]
            print(f"slow: {slow}, fast: {fast}")
            if slow == fast:
                break

        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow

    def findDuplicate_binary_search(self, nums):
        # For [1,2,3,4,5], if we count the number of elements smaller or equal to the current number,
        # We get [1,2,3,4,5]. If there is 1 duplicate: [1,2,3,3,5], then result is [1,2,4,4,5]
        # Therefore, we can locate the smallest number, where the number of elements smaller or equal to it, is bigger than itself
        # Use binary search for faster execution, each iteration we find the mid_point in [1,n] and evaluate that number

        l, r = 0, len(nums) -1

        while l <= r:
            mid = (l + r) // 2
            cnt = sum(n <= mid for n in nums)

            if cnt <= mid:
                l = mid + 1
            else:
                res = mid
                r = mid - 1
        return res



nums = [1,3,4,2,2]
# nums = [2,2,2,2,2]


s = Solution()
res = s.findDuplicate_binary_search(nums)
print(f"Result: {res}")