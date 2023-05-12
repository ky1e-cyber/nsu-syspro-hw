from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        def put(rt: Optional[TreeNode], depth: int):
            nonlocal covert_depth
            if rt == None:
                return

            if depth > covert_depth:
                covert_depth = depth
                lst.append(rt.val)

            put(rt.right, depth + 1)
            put(rt.left, depth + 1)

        lst = []
        covert_depth = 0

        put(root, 1)

        return lst
