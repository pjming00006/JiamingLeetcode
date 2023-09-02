class Solution:

    def find_solution(self, x):
        x = str(x)
        l, r = 0, len(x) - 1
        while l < r:
            if x[l] != x[r]:
                return False
            l += 1
            r -= 1
        return True



def main():
    s = Solution()

    result1 = s.find_solution(121)
    result2 = s.find_solution(12345)
    result3 = s.find_solution(123454321)
    print(result1, result2, result3)


if __name__ == "__main__":
    main()