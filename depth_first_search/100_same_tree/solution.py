"""
Idea

트리 순회
"""

from idlelib.tree import TreeNode
from typing import Optional

from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        p_queue = deque([p])
        q_queue = deque([q])

        while p_queue or q_queue:
            p_node = p_queue.popleft()
            q_node = q_queue.popleft()
            if not p_node and not q_node:
                return True
            if not p_node or not q_node:
                return False
            if p_node.val != q_node.val:
                return False

            left_same = (p_node.left is None) == (q_node.left is None)
            right_same = (p_node.right is None) == (q_node.right is None)
            if not left_same or not right_same:
                return False

            if p_node.left and q_node.left:
                p_queue.append(p_node.left)
                q_queue.append(q_node.left)
            if p_node.right and q_node.right:
                p_queue.append(p_node.right)
                q_queue.append(q_node.right)

        return True
