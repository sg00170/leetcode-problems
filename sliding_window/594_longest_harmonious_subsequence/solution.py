"""
Idea

오름차순 정렬
숫자마다 개수 구해놓기
차이가 1인 숫자들의 개수를 합해서 최대값 구하기
"""

from typing import List


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        max_length = 0
        count = {}

        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1

        previous = nums[0]
        for index, num in enumerate(count):
            if index == 0:
                continue
            if num - previous > 1:
                previous = num
                continue

            max_length = max(max_length, count[num] + count[previous])
            previous = num

        return max_length
