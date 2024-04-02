import pdb

class Solution:

    def find_solution(self, nums):
        """
        If input array is only between 0-9:
        - Find the cumulative counts from 0-9 and store in an array
        - Traversing form the end of input, insert value into the correct position
        - Position index minus 1
        """
        if len(nums) <= 1:
            return nums

        cnts = [0] * 10
        for n in nums:
            cnts[n] += 1

        for i in range(1,len(cnts)):
            cnts[i] = cnts[i-1] + cnts[i]

        print(cnts)

        res = [0] * len(nums)
        for i in range(len(nums)-1, -1, -1):
            res[cnts[nums[i]] - 1] = nums[i]
            cnts[nums[i]] -= 1
        return res


def main():
    s = Solution()
    in_arr = [7,5,3,0,1,3,7,8]

    result1 = s.find_solution(in_arr)

    print(result1)


if __name__ == "__main__":
    main()