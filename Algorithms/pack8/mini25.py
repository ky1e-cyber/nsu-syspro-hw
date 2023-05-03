# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def bst_left_turn(root: TreeNode) -> TreeNode:
    right_subtree = root.right

    root.right = right_subtree.left
    right_subtree.left = root

    return right_subtree

def bst_right_turn(root: TreeNode) -> TreeNode:
    left_subtree = root.left

    root.left = left_subtree.right
    left_subtree.right = root

    return left_subtree


class Solution:

    def balanceBST(self, root: TreeNode) -> TreeNode:
        pass

