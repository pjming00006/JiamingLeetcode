class Solution:

    def find_solution(self, nums):
        """
        Stop condition: when no swap happened within one pass
        """
        if len(nums) <= 1:
            return nums

        end = len(nums) - 1
        if_swap = True

        while if_swap:
            if_swap = False
            curr, next = 0, 1
            while next <= end:
                if nums[next] < nums[curr]:
                    nums[curr], nums[next] = nums[next], nums[curr]
                    if_swap = True
                curr += 1
                next += 1
            end -= 1
        return nums

def main():
    s = Solution()

    result1 = s.find_solution([2,0,6,3,7,0,0,6,5,7])
    print(result1)

    result2 = s.find_solution([2,3,4,5,6,1])
    print(result2)

if __name__ == "__main__":
    main()