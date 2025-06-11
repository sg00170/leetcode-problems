from typing import Optional, List


class TreeNode:
    def __init__(
        self,
        val=0,
        left: Optional["TreeNode"] = None,
        right: Optional["TreeNode"] = None,
    ):
        self.val = val
        self.left = left
        self.right = right


def list_to_tree(data: List[Optional[int]]) -> Optional[TreeNode]:
    if not data:
        return None

    nodes = [TreeNode(val) if val is not None else None for val in data]
    kids = nodes[::-1]
    root = kids.pop()

    for node in nodes:
        if node:
            if kids:
                node.left = kids.pop()
            if kids:
                node.right = kids.pop()

    return root
