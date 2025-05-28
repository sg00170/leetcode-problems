"""
Idea

반대로 순회하면서 이전 것보다 숫자가 작으면 감산, 아니면 가산
"""


class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        sum = 0
        previous = 0
        for char in reversed(s):
            value = roman[char]
            if value < previous:
                sum -= value
            else:
                sum += value
            previous = value

        return sum
