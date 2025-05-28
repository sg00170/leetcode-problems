"""
Idea

# 1: 1 => 1가지
# 2: 1, 1 | 2 => 2가지
# 3: 1, 1, 1 | 1, 2 | 2, 1 => 3가지
# 4: 1, 1, 1, 1 | 1, 1, 2 | 1,2,1 | 2,1,1 | 2, 2  => 5가지
# 5: 1, 1, 1, 1, 1 | 1,1,1,2 | 1,1,2,1 | 1,2,1,1 | 2,1,1,1 | 1,2,2 | 2,1,2 | 2,2,1 => 8가지
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        ways = [0, 1, 2]

        for i in range(3, n + 1):
            ways.append(ways[i - 2] + ways[i - 1])

        return ways[n]
