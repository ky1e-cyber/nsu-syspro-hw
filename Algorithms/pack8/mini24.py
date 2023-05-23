from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        def trim_subtree(rt: Optional[TreeNode]) -> Optional[TreeNode]:
            if rt == None:
                return None
            
            if rt.val < low:
                return trim_subtree(rt.right)
            
            elif rt.val > high:
                return trim_subtree(rt.left)
            

            rt.left = trim_subtree(rt.left)
            rt.right = trim_subtree(rt.right)

            return rt
        
        return trim_subtree(root)
        