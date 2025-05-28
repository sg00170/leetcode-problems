"""
Idea

오름차순 정렬 후 순회하면서 가장 작은 쿠키가 필요한 아이에게 가장 작은 쿠키를 주는 방식
"""

from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        children = 0
        cookies = 0

        while children < len(g) and cookies < len(s):
            if s[cookies] >= g[children]:
                children += 1
            cookies += 1

        return children
