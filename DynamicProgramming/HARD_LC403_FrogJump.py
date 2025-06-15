class Solution:
    def initialWrongSolution(self, stones: List[int]) -> bool:
        """
        1. Start from i = 2
        2. Get is it possible, and how many steps it requires to jump from 0 to 3 using -1, 0, 1 steps
        3. Get is it possible, and how many steps it requires to jump from 1 to 3 using 0, 1, 2 steps
        4. if neither is possible return False
        5. if one is possible, last_last = last, last = current i += 1
        6. if another is possilbe

        """

        def can_jump(curr, prev, step):
            if prev + step == curr or prev + step - 1 == curr or prev + step + 1 == curr:
                return True
            else:
                return False

        prev2_step = 0
        prev1_step = 1

        first_ind = 2
        if first_ind >= len(stones):
            if stones[1] == 1:
                return True
            else:
                return False
        first = stones[first_ind]

        def jump(i):
            nonlocal stones, prev2_step, prev1_step
            if i == len(stones):
                return 1
            prev2, prev1, curr = stones[i - 2], stones[i - 1], stones[i]
            ans = 0
            print(f"i: {i}, elements: {prev2} {prev1} {curr} steps: {prev2_step} {prev1_step}")

            prev2_step_copy, prev1_step_copy = prev2_step, prev1_step
            # if prev2 can jump to curr:
            if can_jump(curr, prev2, prev2_step):
                print("prev2 jump")
                cur_step = curr - prev2
                prev2_step = prev1_step
                prev1_step = cur_step
                print(prev2_step, prev1_step)
                ans = max(jump(i + 1), ans)

            # if prev1 can jump to curr:
            prev2_step, prev1_step = prev2_step_copy, prev1_step_copy
            if can_jump(curr, prev1, prev1_step):
                print("prev1 jump")
                cur_step = curr - prev1
                prev2_step = prev1_step
                prev1_step = cur_step
                print(prev2_step, prev1_step)
                ans = max(jump(i + 1), ans)

            return ans

        return jump(2) == 1


class Solution:
    def canCrossTopDownDPRecursion(self, stones: List[int]) -> bool:
        stone_map = {}
        cache = {}

        for i, s in enumerate(stones):
            stone_map[s] = i

        # @cache
        def jump(i, prev_step):
            nonlocal stones
            # If frog reached the last stone, return True
            if i == len(stones) - 1:
                return True
            # If we already calculated this step, return the result
            if (i, prev_step) in cache.keys():
                return cache[(i, prev_step)]

            cur_stone = stones[i]
            # At current stone, frog can move k-1,k, or k+1 steps
            next_steps = [prev_step - 1, prev_step, prev_step + 1]

            ans = False
            for nxt in next_steps:
                # If the step taken results in landing on a stone
                if cur_stone + nxt in stone_map.keys():
                    next_stone_ind = stone_map[cur_stone + nxt]
                    # If the stone is ahead of current stone
                    if next_stone_ind > i:
                        # Move to next step
                        ans = ans or jump(next_stone_ind, nxt)

            cache[(i, prev_step)] = ans
            return ans

        return jump(0, 0)

    def canCrossBottomUp(self, stones: List[int]) -> bool:
        stone_map = {}
        dp = [[False] * (len(stones) + 1) for i in range(len(stones))]
        dp[0][0] = True

        for i, s in enumerate(stones):
            stone_map[s] = i

        for i in range(len(stones)):
            for k in range(len(stones) + 1):
                # If current i, k combination is not achivable, pass
                if not dp[i][k]:
                    continue
                # If i, k combination is reachable, calculate possible next steps
                for step in [k - 1, k, k + 1]:
                    # Can only jump forward
                    if step <= 0:
                        continue
                    # If jump results in landing on a stone, mark that ind+step as True
                    if stones[i] + step in stone_map.keys():
                        stone_ind = stone_map[stones[i] + step]
                        dp[stone_ind][step] = True

        last_stone_status = dp[len(stones) - 1]

        for s in last_stone_status:
            if s:
                return True
        return False



