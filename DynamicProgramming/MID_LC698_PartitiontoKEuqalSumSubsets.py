"""


"""
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums) % k != 0:
            return False

        target = sum(nums) // k
        visited = [False] * len(nums)

        @cache
        def backtrack(cnt, cur_sum):
            nonlocal target, visited
            # If we found k-1 subset, the remaining sum must be target, so return True
            if cnt == k - 1:
                return True
            # If sum is greater than target, the current combination doesn't work, return False
            if cur_sum > target:
                return False
            # If sum == target, we found a subset, increment cnt and start a new subset
            if cur_sum == target:
                return backtrack(cnt + 1, 0)

            # For element not taken yet, try to add it
            for i in range(len(nums)):
                if not visited[i]:
                    visited[i] = True
                    if backtrack(cnt, cur_sum + nums[i]):
                        return True

                    visited[i] = False

            # If list is done and we haven't return True, then subset not available

            return False

        return backtrack(0, 0)

    def canPartitionKSubsetsBacktrackOptimized(self, nums: List[int], k: int) -> bool:
        """
        - We could sort the input array descending to minimize the recursion calls. If an integer is larger than the
          subset sum target, we can just return False
        - Within 1 subset selection, if an element is not chosen at the current step, it won't be chosen later. We can
          keep track of the index
        """
        if sum(nums) % k != 0:
            return False

        target = sum(nums) // k
        visited = [False] * len(nums)

        nums.sort(reverse=True)

        def backtrack(ind, cnt, cur_sum):
            nonlocal target, visited
            # If we found k-1 subset, the remaining sum must be target, so return True
            if cnt == k - 1:
                return True
            # If sum is greater than target, the current combination doesn't work, return False
            if cur_sum > target:
                return False
            # If sum == target, we found a subset, increment cnt and start a new subset
            if cur_sum == target:
                return backtrack(0, cnt + 1, 0)

            # For element not taken yet, try to add it
            for i in range(len(nums)):
                if not visited[i]:
                    visited[i] = True
                    if backtrack(i + 1, cnt, cur_sum + nums[i]):
                        return True

                    visited[i] = False

            # If list is done and we haven't return True, then subset not available

            return False

        return backtrack(0, 0, 0)