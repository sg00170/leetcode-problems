from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}  # 숫자 → 인덱스 저장

        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], i]  # 이전 인덱스, 현재 인덱스
            num_map[num] = i