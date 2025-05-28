from solution import Solution


def test():
    solution = Solution()
    test_cases = [
        {"g": [1, 2, 3], "s": [1, 1], "expected": 1},
        {"g": [1, 2], "s": [1, 2, 3], "expected": 2},
    ]

    for i, test in enumerate(test_cases):
        result = solution.findContentChildren(test["g"], test["s"])
        assert (
            result == test["expected"]
        ), f"Test case {i+1} failed: expected {test['expected']}, got {result}"
        print(f"Test case {i+1} passed: expected {test['expected']}, got {result}")


if __name__ == "__main__":
    test()
