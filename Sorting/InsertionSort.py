class Solution:

    def find_solution(self, nums):
        """
        1. Divide the array into 2 parts - sorted and not-sorted
        2. Initialize the first element as sorted and the rest as unsorted, use 2 pointers
        3. For each unsorted element, store in a temp data structure
        4. Compare the new element with the last element of the sorted part, if new < sorted, move sorted pointer back to previous element
        5. Process step 4 until sorted element is less than new element or reach the begining of the array
        6. Place new element in the correct place

        """
        if len(nums) <= 1:
            return nums

        for i in range(1, len(nums)):
            # Initialize j as pointer to the sorted part, i as pointer to the unsorted part
            j = i - 1
            temp = nums[i]

            # the j>=0 condition must come first or there is a index error when j = -1
            while j >= 0 and nums[j] > temp:
                nums[j+1] = nums[j]
                j -= 1
            nums[j+1] = temp

        return nums

def main():
    s = Solution()

    result1 = s.find_solution([7,3,8,5,1])
    print(result1)

    # result2 = s.find_solution([2,3,4,5,6,1])
    # print(result2)

if __name__ == "__main__":
    main()