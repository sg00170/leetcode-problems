from solution2 import Solution


def test():
    solution = Solution()
    test_cases = [
        {"s": "III", "expected": 3},
        {"s": "LVIII", "expected": 58},
        {"s": "MCMXCIV", "expected": 1994},
    ]

    for i, test in enumerate(test_cases):
        result = solution.romanToInt(test["s"])
        assert (
            result == test["expected"]
        ), f"Test case {i+1} failed: expected {test['expected']}, got {result}"
        print(f"Test case {i+1} passed: expected {test['expected']}, got {result}")


if __name__ == "__main__":
    test()
