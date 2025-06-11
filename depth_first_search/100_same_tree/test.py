import sys
import os

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
sys.path.insert(0, ROOT_DIR)

from solution import Solution
from utils.tree_node import list_to_tree


def test():
    solution = Solution()
    test_cases = [
        {"p": [], "q": [], "expected": True},
        {"p": [1, 2, 3], "q": [1, 2, 3], "expected": True},
        {"p": [1, 2], "q": [1, None, 2], "expected": False},
        {"p": [1, 2, 1], "q": [1, 1, 2], "expected": False},
    ]

    for i, test in enumerate(test_cases):
        p_tree = list_to_tree(test["p"])
        q_tree = list_to_tree(test["q"])
        result = solution.isSameTree(p_tree, q_tree)
        assert (
            result == test["expected"]
        ), f"Test case {i+1} failed: expected {test['expected']}, got {result}"
        print(f"Test case {i+1} passed: expected {test['expected']}, got {result}")


if __name__ == "__main__":
    test()
