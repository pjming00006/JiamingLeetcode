class Solution:
    """
    Two Pointer + Recursion

    left pointer iterate through the array, right pointer starts the same position as left and goes til the end
    recursive until right pointer reach the last element of the list

    [1,2,3]
    initially: i = 0
    swap[0,0], [0,1], [0,2] --> [1,2,3], [2,1,3], [3,2,1]

    i = 1, swap [1,1], [1,2]
    [1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,2,1], [3,1,2]

    i = 2, record the result

    Algorithms:
    1. When i = len(nums) - 1, return value
    2. Swap i and j
    3. increment j and i
    """
    def find_solution(self, nums, l):
        res = []

        def recur(nums, l):
            if l == len(nums)-1:
                res.append(nums.copy())
                return
            else:
                for r in range(l, len(nums)):
                    nums[l], nums[r] = nums[r], nums[l]
                    recur(nums, l+1)
                    nums[l], nums[r] = nums[r], nums[l]
        recur(nums, 0)
        return res


def main():
    s = Solution()
    result = s.find_solution([1,2], 0)
    print(result)
    result = s.find_solution([1, 2, 4], 0)
    print(result)


if __name__ == "__main__":
    main()