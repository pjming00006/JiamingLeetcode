"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.



Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.


Constraints:

1 <= prices.length <= 105
0 <= prices[i] <= 104
"""


class Solution:
    def maxProfitBruteForce(self, prices: list[int]) -> int:
        """
        Time: O(n^2): For each element, we loop through the rest of the array
        Space: O(1): space required does not depend on the size of input array
        """
        cur_max = 0
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                cur_max = max(prices[j] - prices[i], cur_max)
        return cur_max

    def maxProfitTwoPointerSimplified(self, prices: list[int]) -> int:
        """
        Time: O(n), Space: O(1)
        """
        p1, p2 = 0, 1
        maxprofit = 0
        while p2 < len(prices):
            maxprofit = max(maxprofit, prices[p2] - prices[p1])
            if prices[p2] < prices[p1]:
                p1 = p2
            p2 += 1
        return maxprofit

    def maxProfitOnePass(self, prices: list[int]) -> int:
        """Same as two pointers but not implementing the actual pointers"""
        minprice = prices[0]
        maxprofit = 0

        for i in range(1, len(prices)):
            maxprofit = max(maxprofit, prices[i] - minprice)
            minprice = min(minprice, prices[i])
        return maxprofit



obj = Solution()
res = obj.maxProfitTwoPointer([7,1,5,3,6,4])
print(res)

res = obj.maxProfitTwoPointer([7,6,4,3,1])
print(res)

res = obj.maxProfitTwoPointer([1,2,4,2,5,7,2,4,9,0,9])
print(res)
