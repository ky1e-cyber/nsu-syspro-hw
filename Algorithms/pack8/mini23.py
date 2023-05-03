from typing import Optional

MIN_INT = -(2 ** 31)
MAX_INT = (2 ** 31) - 1

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True

        def is_valid_subtree(rt: Optional[TreeNode], low: int, high: int) -> bool:
            if rt == None:
                return True

            return (
                (rt.val > low and rt.val < high) and 
                is_valid_subtree(rt.left, low, rt.val) and 
                is_valid_subtree(rt.right, rt.val, high)
            )

        return (
            is_valid_subtree(root.left, MIN_INT - 1, root.val) and 
            is_valid_subtree(root.right, root.val, MAX_INT + 1)
        )
