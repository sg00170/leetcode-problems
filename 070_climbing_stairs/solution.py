# You are climbing a staircase.
# It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps.
# In how many distinct ways can you climb to the top?
#
# Example 1: Input: n = 2
# Output: 2 Explanation:
# There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
#
# Example 2: Input: n = 3 Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step

# Idea
# 1: 1 => 1
# 2: 1, 1 | 2 => 2
# 3: 1, 1, 1 | 1, 2 | 2, 1 => 3
# 4: 1, 1, 1, 1 | 1, 1, 2 | 1,2,1 | 2,1,1 | 2, 2  => 5
# 5: 1, 1, 1, 1, 1 | 1,1,1,2 | 1,1,2,1 | 1,2,1,1 | 2,1,1,1 | 1,2,2 | 2,1,2 | 2,2,1 => 8


class Solution:
    def climbStairs(self, n: int) -> int:
        ways = [0, 1, 2]

        for i in range(3, n + 1):
            ways.append(ways[i - 2] + ways[i - 1])

        return ways[n]
