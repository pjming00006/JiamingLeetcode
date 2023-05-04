class Solution:

    def find_solution_recursive(self, nums, target):
        """
        find the middle row of the matrix
        get left and right most item in the row.
        if target within the row, binary search the row
        if not, binary search the remaining matrix and repeat
        """

        def b_search_row(nums, target):
            l, r = 0, len(nums) - 1
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] == target:
                    return True
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return False

        def b_search_matrix(nums, target, l, r):
            while l <= r:
                mid = (l + r) // 2
                mid_mtx = nums[mid]

                row_l, row_r = 0, len(mid_mtx) - 1
                if mid_mtx[row_l] <= target <= mid_mtx[row_r]:
                    print("do binary search within row")
                    print(mid_mtx)
                    return b_search_row(mid_mtx, target)
                elif target < mid_mtx[row_l]:
                    print("matrix search left")
                    return b_search_matrix(nums, target, l, mid-1)
                elif target > mid_mtx[row_r]:
                    print("matrix search right")
                    return b_search_matrix(nums, target, mid+1, r)

        l, r = 0, len(nums) - 1
        return b_search_matrix(nums, target, l, r)




def main():
    s = Solution()

    # result1 = s.find_solution([1,2,3,4,5,5,5,5,5,5,7,8], 5)
    # print(result1)
    #
    # result2 = s.find_solution([5,5,5,5,5,5], 5)
    # print(result2)

    result1 = s.find_solution_recursive([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3)
    print(result1)


if __name__ == "__main__":
    main()