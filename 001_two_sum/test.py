from solution import Solution

def test():
    solution = Solution()
    test_cases = [
        {"nums": [2, 7, 11, 15], "target": 9, "expected": [0, 1]},
        {"nums": [3, 2, 4], "target": 6, "expected": [1, 2]},
        {"nums": [3, 3], "target": 6, "expected": [0, 1]},
    ]

    for i, test in enumerate(test_cases):
        result = solution.twoSum(test["nums"], test["target"])
        assert result == test["expected"], f"Test case {i+1} failed: expected {test['expected']}, got {result}"
        print(f"Test case {i+1} passed: expected {test['expected']}, got {result}")

if __name__ == "__main__":
    test()
