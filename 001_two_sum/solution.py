from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        N = len(nums)
        indices = []

        for i in range(N):
            for j in range(i + 1, N):
                if nums[i] + nums[j] == target:
                    return [i, j]

        return indices
