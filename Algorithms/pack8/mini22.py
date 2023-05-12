from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def get_subtree(rt: TreeNode, curr_height) -> Optional[TreeNode]:
            local_height = 0

            while local_height <= curr_height:
                if rt.right is not None:
                    rt = rt.right
                elif rt.left is not None:
                    rt = rt.left
                else:
                    return None
                local_height += 1
            
            return rt
            

        def put_subtree(rt: Optional[TreeNode], height: int) -> int:
            if rt == None:
                return height
            


        def put_subtree(rt: Optional[TreeNode]):
            if rt == None:
                return
            
            lst.append(rt.val)
            curr_height += 1

            nxt = get_subtree(rt)

            if nxt is None:
                return
            
            curr_height += 1
            lst.append(rt.val)
            put_subtree(rt.right)
            

        lst = []
