class Solution:

    def find_solution(self, nums, target):
        l, r = 0, len(nums) -1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            # if number at left point is smaller or equal to number at mid, then left part is sorted
            if nums[l] <= nums[mid]:
                # if target is within the left part, evaluate the left part
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else: # else evaluate the right part
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1


def main():
    s = Solution()

    result1 = s.find_solution([4,5,6,7,0,1,2], 0)
    print(result1)

    result2 = s.find_solution([4,5,6,7,0,1,2], 3)
    print(result2)

if __name__ == "__main__":
    main()