"""
Key observation: 
when we encounter a new temperature, 2 possilbe actions:
1. If temperature is high then we need to update previous days to reflect days it takes for higher temp
    - We are not only updating the most recent day, but all days that had lower temperatures, until there
    is none
2. If temperature is low then we add to the unprocessed list and keep going

Monotonic decreasing stack
"""
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Space complexity O(n) since we maintain an extra stack that can be O(n) if
        # temperatures always decrease
        out = [0] * len(temperatures)

        stack = [0]

        for curr_ind in range(1, len(temperatures)):
            curr_temp = temperatures[curr_ind]

            # While current temperature is higher than top of stack, keep popping and
            # updating output array
            while stack and curr_temp > temperatures[stack[-1]]:
                prev_ind = stack.pop()
                out[prev_ind] = curr_ind - prev_ind
            
            # if not higher than top of stack, append to stack
            stack.append(curr_ind)
        return out
    
    def dailyTemperaturesLoopBackward(self, temperatures: List[int]) -> List[int]:
        """
        In this appraoch, we use the output array to provide valuable information and loop backwards.

        For each day, we try to find a future day where temperature is higher, utilizing the output
        array. If there is one, we record the index difference. If there isn't, we continue to next
        element.

        This approach has space complexity O(1) since no extra space is used besides output array
        """
        out = [0] * len(temperatures)

        for curr_ind in range(len(temperatures) -2, -1, -1):
            # For each day, we look at next day to see if temperature is higher
            curr_temp = temperatures[curr_ind]
            
            # Start by comparing with the next day
            next_ind = curr_ind + 1

            # While next day's temperature is lower, we try to find a day with higher temperature
            while temperatures[next_ind] <= curr_temp:
                # If there isn't a higher temperature day, stop looking
                if out[next_ind] == 0:
                    break
                # The index of day where temperture is even higher than next day's
                next_ind += out[next_ind]
            
            # If we manage to find a future day with higher temperature, record the index
            if temperatures[next_ind] > curr_temp:
                out[curr_ind] = next_ind - curr_ind
        
        return out