"""
Idea

로마자 배열을 만든 후 문자열을 순회하면서 정수값 합산
"""


class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
            "CM": 900,
            "CD": 400,
            "XC": 90,
            "XL": 40,
            "IX": 9,
            "IV": 4,
        }

        S = len(s)
        i = 0
        sum = 0
        while i < S:
            if (i + 1) < S and (s[i] + s[i + 1]) in roman:
                sum += roman[s[i] + s[i + 1]]
                i += 1
            else:
                sum += roman[s[i]]
            i += 1

        return sum
