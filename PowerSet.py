class Solution:
    """
    Given integer array, return all possible subsets(power sets)
    in: [1,2]
    out: [[], [1], [2], [1,2]]

    in: [1,2,3]
    out: [[],[1],[2],[3],[1,2],[1,3],[2,3],[1,2,3]]

    For any given element, there are 2 options: include the element, or not
    Therefore, there is always 2^n elements in the result, where n is size of array
    """

    def find_solution_iterative(self, nums):
        # res = [[]]
        # for n in nums:
        #     new_res = []
        #     for res_set in res:
        #         new_set = res_set.copy()
        #         new_set.append(n)
        #         new_res.append(new_set)
        #     res = res + new_res
        #
        # return res

        res = [[]]
        for n in nums:
            res += [r + [n] for r in res]
        return res

    def find_solution_recursive(self, nums):
        result = []
        def recur(ind, nums, res):
            if ind == len(nums):
                print(res)
                result.append(res.copy())
                return
            recur(ind+1, nums, res)
            res.append(nums[ind])
            recur(ind+1, nums, res)
            res.pop()
        recur(0, nums, [])
        print(result)



def main():
    s = Solution()
    # result = s.find_solution_iterative([1, 2, 5, 7, 9])

    result = s.find_solution_recursive([1,8,7])
    print(result)


if __name__ == "__main__":
    main()