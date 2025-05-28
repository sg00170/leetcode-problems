"""
Idea

순회 해서 두 숫자를 합했을 때 target이 된다면 해당 숫자들의 배열 index 반환
"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        N = len(nums)

        for i in range(N):
            for j in range(i + 1, N):
                if nums[i] + nums[j] == target:
                    return [i, j]
