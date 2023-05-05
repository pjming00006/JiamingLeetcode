class Solution:

    def find_solution(self, nums):
        """
        i. Given input array, find mid point
        ii. Break the array into 2 parts and feed into the recursive function
        iii. Stop criteria: when array length is 1 Then, merge the 2 arrays
        """
        if len(nums) <= 1:
            return nums

        mid = len(nums) // 2
        left_arr = self.find_solution(nums[:mid])
        right_arr = self.find_solution(nums[mid:])

        # perform merge
        l, r = 0, 0
        res = []
        while l < len(left_arr) and r < len(right_arr):
            if left_arr[l] < right_arr[r]:
                res.append(left_arr[l])
                l += 1
            else:
                res.append(right_arr[r])
                r += 1

        if l <= len(left_arr):
            res += left_arr[l:]
        if r <= len(right_arr):
            res += right_arr[r:]

        return res


def main():
    s = Solution()

    result1 = s.find_solution([4,8,2,6,1,5])
    print(result1)

    result2 = s.find_solution([2,3,4,5,6,1,8])
    print(result2)

if __name__ == "__main__":
    main()