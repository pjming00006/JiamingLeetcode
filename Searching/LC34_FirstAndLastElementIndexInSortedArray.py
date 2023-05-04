class Solution:

    def find_solution(self, nums, target):
        """
        use binary search 2 times to find left extremes and right extremes
        """

        def find_left(nums, target):
            l, r = 0, len(nums) - 1
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] == target:
                    if mid == 0:
                        return mid
                    else:
                        if nums[mid-1] != target:
                            return mid
                        else:
                            r = mid - 1

                elif nums[mid] > target:
                    r = mid - 1
                elif nums[mid] < target:
                    l = mid + 1
            return -1

        def find_right(nums, target):
            l, r = 0, len(nums) -1
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] == target:
                    if mid == len(nums)-1:
                        return mid
                    else:
                        if nums[mid+1] != target:
                            return mid
                        else:
                            l = mid + 1

                elif nums[mid] > target:
                    r = mid - 1
                elif nums[mid] < target:
                    l = mid + 1
            return -1
        res = [find_left(nums, target), find_right(nums, target)]

        return res

    def find_solution_recursive(self, nums, target):
        """
        use binary search 2 times to find left extremes and right extremes
        """

        def find_left_recur(nums, target, l, r):
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] == target:
                    if mid == 0:
                        return mid
                    else:
                        if nums[mid-1] != target:
                            return mid
                        else:
                            return find_left_recur(nums, target, l, mid-1)

                elif nums[mid] > target:
                    return find_left_recur(nums, target, l, mid-1)
                elif nums[mid] < target:
                    return find_left_recur(nums, target, mid + 1, r)
            return -1

        def find_right_recur(nums, target, l, r):
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] == target:
                    if mid == len(nums)-1:
                        return mid
                    else:
                        if nums[mid+1] != target:
                            return mid
                        else:
                            return find_right_recur(nums, target, mid+1, r)

                elif nums[mid] > target:
                    return find_right_recur(nums, target, l, mid-1)
                elif nums[mid] < target:
                    return find_right_recur(nums, target, mid+1, r)
            return -1

        l, r = 0, len(nums) - 1
        res = [find_left_recur(nums, target, l, r), find_right_recur(nums, target, l, r)]

        return res


def main():
    s = Solution()

    # result1 = s.find_solution([1,2,3,4,5,5,5,5,5,5,7,8], 5)
    # print(result1)
    #
    # result2 = s.find_solution([5,5,5,5,5,5], 5)
    # print(result2)

    result1 = s.find_solution_recursive([1,2,3,4,5,5,5,5,5,5,7,8], 5)
    print(result1)

    result2 = s.find_solution_recursive([5,5,5,5,5,5], 5)
    print(result2)

if __name__ == "__main__":
    main()