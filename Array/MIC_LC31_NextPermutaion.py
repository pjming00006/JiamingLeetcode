"""
A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

For example, for arr = [1,2,3], the following are all the permutations of arr: [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].
The next permutation of an array of integers is the next lexicographically greater permutation of its integer. More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, then the next permutation of that array is the permutation that follows it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

For example, the next permutation of arr = [1,2,3] is [1,3,2].
Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.
Given an array of integers nums, find the next permutation of nums.

The replacement must be in place and use only constant extra memory.

 

Example 1:

Input: nums = [1,2,3]
Output: [1,3,2]
Example 2:

Input: nums = [3,2,1]
Output: [1,2,3]
Example 3:

Input: nums = [1,1,5]
Output: [1,5,1]
 

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 100
"""

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Critical Observations
        1. To get next permutation, if we put the list into a number, the next permutation number must be greater than the current one, 
           except for cases where the order of number is strictly decreasing, where we need to reverse it
        2. We are not only getting a larger number, we are getting THE NEXT, meaning that the number needs to increase but it should 
           be minimally increase
        
        To get a larger number:
        - We can swap a larger digit in the back to a fronter location. For example, for [1, 2, 3, 9, 8, 7], swap 7 with 3, then re-arrage [9, 8, 3]
          into [3, 8, 9], to get [1, 2, 7, 3, 8, 9]
        - In this case, 3 is the pivot, it's the first case where num[i] < num[i+1] when evaluating from the right
        - But, do we always want to swap pivot with the last digit?
          - Ideally, but only when the number at last is larger than the pivot; if it's smaller, then swapping won't create a larger number
          - Therefore, we move the right pointer to left until there is a candidate
        
        After swapping, we need to reverse the reamining to be ascending
        """
        def swap(left, right):
            num_left, num_right = nums[left], nums[right]
            nums[left], nums[right] = num_right, num_left
        
        def reverse(left, right):
            while left < right:
                swap(left, right)
                left += 1
                right -= 1

        left, right = len(nums) - 2, len(nums) - 1

        # Find pivot using left pointer
        while left >= 0 and nums[left] >= nums[left + 1]:
            left -= 1
        
        if left >= 0:
            # Find the right element for swapping
            while nums[right] <= nums[left]:
                right -= 1
            swap(left, right)
        
        reverse(left + 1, len(nums) - 1)

