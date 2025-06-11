from solution2 import Solution


def test():
    solution = Solution()
    test_cases = [
        {"nums": [1, 3, 2, 2, 5, 2, 3, 7], "expected": 5},
        {"nums": [1, 2, 3, 4], "expected": 2},
        {"nums": [1, 1, 1, 1], "expected": 0},
    ]

    for i, test in enumerate(test_cases):
        result = solution.findLHS(test["nums"])
        assert (
            result == test["expected"]
        ), f"Test case {i+1} failed: expected {test['expected']}, got {result}"
        print(f"Test case {i+1} passed: expected {test['expected']}, got {result}")


if __name__ == "__main__":
    test()
