# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from typing import List, Optional

class Codec:

    SEPARATOR = ","
    NULL_TOKEN = "null"

    def push(lst: List[str], ind: int, el: Optional[str]):
        if el is None:
            el = Codec.NULL_TOKEN

        while len(lst) <= ind:
            lst.append(Codec.NULL_TOKEN)

        lst[ind] = el

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root == None:
            return Codec.NULL_TOKEN

        def put_subtree(root: TreeNode, ind: int):
            Codec.push(lst, ind, str(root.val))
            if not (root.left is None):
                put_subtree(root.left, 2 * ind + 1)
            if not (root.right is None):
                put_subtree(root.right, 2 * ind + 2)
        
        lst = []
        put_subtree(root, 0)


        return (Codec.SEPARATOR).join(lst)

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """

        def get_subtree(ind) -> Optional[TreeNode]:
            if (len(lst) <= ind) or (lst[ind] == Codec.NULL_TOKEN):
                return None
            
            root = TreeNode(int(lst[ind]))

            root.left = get_subtree(2 * ind + 1)
            root.right = get_subtree(2 * ind + 2)

            return root

        lst = data.split(Codec.SEPARATOR)
        return get_subtree(0)
