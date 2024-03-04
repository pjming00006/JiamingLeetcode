"""
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.



Example 1:

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
Example 2:

Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]
Example 3:

Input: temperatures = [30,60,90]
Output: [1,1,0]


Constraints:

1 <= temperatures.length <= 105
30 <= temperatures[i] <= 100
"""


class Solution:
    def dailyTemperaturesBruteForce(self, temperatures: list[int]) -> list[int]:
        """
        For each element, loop through the rest of the array on the right until a higher temperature appears
        """
        res = [0] * len(temperatures)
        for i in range(len(temperatures)):
            for j in range(i+1, len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    res[i] = j-i
                    break
        return res

    def dailyTemperaturesRightMax(self, temperatures: list[int]) -> list[int]:
        """
        Still brute force but making some improvements

        Start from the end of array, keep a record of the maximum encountered. If current element is less than max
            then there is an answer. Otherwise, it's 0
        """
        res = [0] * len(temperatures)
        cur_max = temperatures[-1]

        for i in range(len(temperatures)-2, -1, -1):
            if temperatures[i] < cur_max:
                for j in range(i+1, len(temperatures)):
                    if temperatures[j] > temperatures[i]:
                        res[i] = j - i
                        break
            else:
                cur_max = temperatures[i]
        return res

    def dailyTemperaturesRightDynamic(self, temperatures: list[int]) -> list[int]:
        """
        We can make use of the partial output that gets created
        - For every index from right, we check if the next element is greater
        - If not, then we look at the partial output and find out the index of the next greater for the next element
        - We keep looking right until we found that element and record the difference in index as the answer
        """
        res = [0] * len(temperatures)

        for i in range(len(temperatures)-2, -1, -1):
            next_ind = i + 1
            if temperatures[next_ind] <= temperatures[i] and res[next_ind] == 0:
                res[i] = 0
            else:
                while temperatures[next_ind] <= temperatures[i]:
                    next_ind += res[next_ind]
                res[i] = next_ind - i
        return res

    def dailyTemperaturesStack(self, temperatures: list[int]) -> list[int]:
        """
        The above answer is better but still has improvements.
        - The 3 solutions above all require us to loop through the elements we already visited for the answer, which
            is inefficient.
        - Plus, there is an important property:
           *** we are looking for the next element that is greater.
           *** consider [70, 75, 73]: If second element is greater than the third, then the third can never be
           *** the next greater element for 70. So if we encounter 75, then 73 can be discarded.
        """

        res = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)-1, -1, -1):
            while stack and temperatures[i] >= temperatures[stack[-1]]:
                stack.pop()
            if stack:
                res[i] = stack[-1] - i
            stack.append(i)
        return res






s = Solution()
res = s.dailyTemperaturesStack([73,74,75,71,69,72,76,73])  # [1,1,4,2,1,1,0,0]
print(res)
#
# res = s.dailyTemperaturesBruteForce([30,40,50,60])
# print(res)
#
# res = s.dailyTemperaturesBruteForce([30,60,90])
# print(res)

res = s.dailyTemperaturesBruteForce([55,38,53,81,61,93,97,32,43,78])
print(res)