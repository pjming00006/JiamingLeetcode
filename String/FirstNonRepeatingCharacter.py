class Solution:
    """
    Given integer array, return all possible subsets(power sets)
    """

    def find_solution_brute_force(self, str):
        for i in range(len(str)):
            non_repeat = True
            for j in range(len(str)):
                if i == j:
                    continue
                else:
                    if str[i] == str[j]:
                        non_repeat = False
                        break
            if non_repeat:
                return i
        return -1

    def find_solution_hash(self, str):
        occur_dict = {}
        for i in range(len(str)):
            if str[i] not in occur_dict.keys():
                occur_dict[str[i]] = 1
            else:
                occur_dict[str[i]] += 1

        print(occur_dict)
        for i in range(len(str)):
            if occur_dict[str[i]] == 1:
                return i
        return -1



def main():
    s = Solution()

    # result1 = s.find_solution_brute_force("AabcAcbd")
    # result2 = s.find_solution_brute_force("aabb33")
    # result3 = s.find_solution_brute_force("abA")
    # print(result1, result2, result3)

    result1 = s.find_solution_hash("AabcAcbd")
    result2 = s.find_solution_hash("aabb33")
    result3 = s.find_solution_hash("abA")
    print(result1, result2, result3)


if __name__ == "__main__":
    main()