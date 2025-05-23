from solution import Solution


def test():
    solution = Solution()
    test_cases = [
        {"n": 2, "expected": 2},
        {"n": 3, "expected": 3},
    ]
    for i, test in enumerate(test_cases):
        result = solution.climbStairs(test["n"])
        assert (
            result == test["expected"]
        ), f"Test case {i+1} failed: expected {test['expected']}, got {result}"
        print(f"Test case {i+1} passed: expected {test['expected']}, got {result}")


if __name__ == "__main__":
    test()
