class Solution:

    def find_solution_recursive(self, nums, target):
        """
        1. find middle point
        2. compare with target
        3. if mid < target, get latter half; if mid > target, get earlier half
        4. recursive

        Note that this method uses more space since we are assigning new values for left and right for each stack
        """
        def recur(nums, l, r):
            if l > r:
                return -1
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                return recur(nums, l, mid - 1)
            elif nums[mid] < target:
                return recur(nums, mid + 1, r)
        return recur(nums, 0, len(nums)-1)

    def find_solution(self, nums, target):
        l, r = 0, len(nums) -1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            print(l, r, mid)
        return -1


def main():
    s = Solution()

    result1 = s.find_solution_recursive([-1,0,3,5,9,12], 9)
    print(result1)

    result2 = s.find_solution_recursive([-1, 0, 3, 5, 9, 12, 15], 15)
    print(result2)

if __name__ == "__main__":
    main()