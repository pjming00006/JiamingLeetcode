class Solution:

    def find_solution(self, nums):
        """
        i. Use 2 pointers, for each I, loop through using pointer j to find the index of the smallest item
        ii. Swap the smallest item with the first item
        iii. Stop when there is no more swap or i-pointer reaches end
        """
        if len(nums) <= 1:
            return nums

        for i in range(len(nums)-1):
            j = i + 1
            local_min_ind = i
            while j < len(nums):
                if nums[j] < nums[local_min_ind]:
                    local_min_ind = j
                j += 1
            if local_min_ind != i:
                nums[i], nums[local_min_ind] = nums[local_min_ind], nums[i]
        return nums


def main():
    s = Solution()

    result1 = s.find_solution([4,8,2,6,1,5])
    print(result1)

    result2 = s.find_solution([2,3,4,5,6,1])
    print(result2)

if __name__ == "__main__":
    main()