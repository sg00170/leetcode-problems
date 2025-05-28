"""
Idea

target과 현재 값의 차를 구하고, 해당 값이 저장해놓은 map에 있다면 두 숫자의 index 반환
"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], i]
            num_map[num] = i
