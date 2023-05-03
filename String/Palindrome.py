class Solution:

    def find_solution(self, str):
        l, r = 0, len(str) - 1
        while l < r:
            if str[l] != str[r]:
                return False
            l += 1
            r -= 1
        return True



def main():
    s = Solution()

    result1 = s.find_solution("abcba")
    result2 = s.find_solution("aaaaaa")
    result3 = s.find_solution("abcdefghijklmn")
    print(result1, result2, result3)


if __name__ == "__main__":
    main()