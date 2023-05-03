from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def get_next(node: TreeNode) -> Optional[TreeNode]:
            return (
                node.left 
                if node.right is None 
                else node.right
            )
    
        def get_from_right(rt: TreeNode):
            while rt is not None:
                yield rt.val
                rt = get_next(rt)
        
        def get_from_left(rt: TreeNode, height: int):
            curr_height = 0
            while (rt is not None) and (curr_height <= height):
                rt = get_next(rt)
                curr_height += 1
            while rt is not None:
                yield rt.val
                rt = get_next(rt)

        if root == None:
            return []
        
        rights = list(
            get_from_right(root.right) 
            if root.right is not None 
            else []
        )

        lefts = list(
            get_from_left(root.left, len(rights)) 
            if root.left is not None 
            else []
        )

        return [root.val] + rights + lefts
        