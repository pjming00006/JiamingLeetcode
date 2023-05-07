import pdb

class Solution:

    def counting_sort(self, nums, digit):
        def find_digit(n, d):
            if len(str(n)) >= d:
                return int(str(n)[-d])
            else:
                return 0

        cnts = [0] * 10
        for n in nums:
            cnts[find_digit(n, digit)] += 1

        for i in range(1,len(cnts)):
            cnts[i] = cnts[i-1] + cnts[i]

        res = [0] * len(nums)
        for i in range(len(nums)-1, -1, -1):
            val = find_digit(nums[i], digit)
            res[cnts[val]-1] = nums[i]
            cnts[val] -= 1
        print(f"After the sort on digit {digit}: {res}")

        return res

    def find_solution(self, nums):
        if len(nums) <= 1:
            return nums

        max_digit = 1
        for n in nums:
            max_digit = max(max_digit, len(str(n)))
        print(max_digit)

        for i in range(1, max_digit+1):
            print(f"Counting sort with digit {i}")
            nums = self.counting_sort(nums, i)
        return nums



def main():
    s = Solution()
    in_arr = [384,72,1023,374,183,65,247,185,5,1024]

    print(in_arr)
    result1 = s.find_solution(in_arr)

    print(result1)


if __name__ == "__main__":
    main()