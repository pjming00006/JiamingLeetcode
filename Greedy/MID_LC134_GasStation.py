"""
There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next (i + 1)th station. You begin the journey with an empty tank at one of the gas stations.

Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1. If there exists a solution, it is guaranteed to be unique.

 

Example 1:

Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
Output: 3
Explanation:
Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 4. Your tank = 4 - 1 + 5 = 8
Travel to station 0. Your tank = 8 - 2 + 1 = 7
Travel to station 1. Your tank = 7 - 3 + 2 = 6
Travel to station 2. Your tank = 6 - 4 + 3 = 5
Travel to station 3. The cost is 5. Your gas is just enough to travel back to station 3.
Therefore, return 3 as the starting index.
Example 2:

Input: gas = [2,3,4], cost = [3,4,3]
Output: -1
Explanation:
You can't start at station 0 or 1, as there is not enough gas to travel to the next station.
Let's start at station 2 and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 0. Your tank = 4 - 3 + 2 = 3
Travel to station 1. Your tank = 3 - 3 + 3 = 3
You cannot travel back to station 2, as it requires 4 unit of gas but you only have 3.
Therefore, you can't travel around the circuit once no matter where you start.
 

Constraints:

n == gas.length == cost.length
1 <= n <= 105
0 <= gas[i], cost[i] <= 104
The input is generated such that the answer is unique.
"""

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """
        Critical observation:
        1. If sum of gas < sum of cost, then it's impossible to have an answer
        2. If route that starts from i until j fails, it means that all routes from k to j, where i<=k<=j, would fail. This is because I start
           from i with 0 gas(worst possible scenario for a possible route). This means that I can skip those indexes as start index
           - What should be next index? j+1, because at j it fails, it menas that remaining gas + gas[j] - cost[j] < 0
        
        3. When I reach last element as start, and locally remaining gas + gas[j] - cost[j] > 0, how to make sure that remaining route is valid?
           a. At start, we checked to ensure sum(gas) >= sum(cost)
           b. When reaching the last element as start, we negated all previous elements as start. It means that the sum of all previous gas is less
             than sum of all previous costs. But since (a) is true, it means starting from last element has to succeed
        """

        if sum(gas) < sum(cost):
            return -1

        remaining_gas = 0
        start_ind = 0
        for i in range(len(gas)):
            remaining_gas = remaining_gas + gas[i] - cost[i]
            if remaining_gas < 0:
                start_ind = i + 1
                remaining_gas = 0
        
        return start_ind