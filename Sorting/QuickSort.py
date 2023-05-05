import pdb

class Solution:

    def find_solution(self, nums):
        """
        Select a pivot as the base of the comparison
        Initialize 2 pointers, the left pointer moves to the right until there is a element greater than the pivot
        The right pointer moves to the left until there is a element smaller than the pivot
        Swap the 2 elements
        Keep looping until left < right
        Swap pivot with the last element that is smaller than it
        Recursively call the function on left side and right side
        """
        if len(nums) <= 1:
            return nums
        print(f"Current array: {nums}")
        pivot_ind = 0
        l, r = 1, len(nums) - 1

        while l <= r:
            while l < len(nums) and nums[l] <= nums[pivot_ind]:
                l += 1
            while r >= 0 and nums[r] >= nums[pivot_ind]:
                r -= 1

            if l < r:
                nums[l], nums[r] = nums[r], nums[l]
            else:
                nums[pivot_ind], nums[l-1] = nums[l-1], nums[pivot_ind]

        left_arr = self.find_solution(nums[:l-1])
        right_arr = self.find_solution(nums[l:])

        res = left_arr + [nums[l-1]] + right_arr
        return res


def main():
    s = Solution()
    in_arr = [14,22,12,18,19,11,8,13,9]

    print(in_arr)
    result1 = s.find_solution(in_arr)

    print(result1)

    # result2 = s.find_solution([2,3,4,5,6,1,8])
    # print(result2)

if __name__ == "__main__":
    main()