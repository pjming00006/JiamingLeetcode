
"""
Key Obeservation:
If we execute the same tasks together, then we suffer from the idle time because they are not utilized
to execute other tasks. More importantly, if we leave the higher frequency tasks unhandled, then will
cluster together, and idle times would not be utilized.

Therefore, it's important to schedule higher frequency tasks earlier when possible.

This allows the usage of a greedy algorithm, where we always prioritize the task with highest frequency,
using a max heap.
"""

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        import heapq

        # Build a frequency map
        freq = [0]*26
        for t in tasks:
            freq[ord(t) - ord("A")] += 1
        
        # Create a max heap with non-zero tasks
        q = [-f for f in freq if f > 0]
        heapq.heapify(q)

        time = 0

        while q:
            # cyle denotes a fixed internal representing the cool down required
            cycle = n + 1
            task_count = 0 # count of task implemented during cycle
            next_heap = []

            while cycle > 0 and q:
                # Pop the task with highest frequency
                cur_freq = -heapq.heappop(q)
                # Increment task count, decrement remaining cool down period
                task_count += 1
                cycle -= 1
                # If this task type still have remainings, add it back to next heap
                if cur_freq > 1:
                    next_heap.append(-(cur_freq - 1))
            
            # If all tasks are finished, only add task count to time
            # If there are more tasks, always add the cycle to time(n+1)
            time += task_count if not next_heap else n+1

            for h in next_heap:
                heapq.heappush(q, h)

        return time


