from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        def find_lowest(rt: TreeNode):
            if rt.val < low:
                return 
            
        low_node = None

        curr_node = root

        while (curr_node.val >= low) and (curr_node.left is not None):
            low_node = curr_node
            curr_node = curr_node.left

        while (curr_node.val < low) and (curr_node.right is not None):
            curr_node = curr_node.right
        