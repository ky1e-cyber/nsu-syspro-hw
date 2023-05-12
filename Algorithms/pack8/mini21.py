from collections import deque
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    SEPARATOR = ","
    NULL_TOKEN = "null"

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """

        def push(rt: Optional[TreeNode]):
            if rt == None:
                stack.append(Codec.NULL_TOKEN)
            else:
                stack.append(str(rt.val))
                push(rt.left)
                push(rt.right)

        stack = deque()
        push(root)
        return (Codec.SEPARATOR).join(stack)

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """

        def get_subtree() -> Optional[TreeNode]:
            if len(stack) == 0:
                return None

            nxt: Optional[int] = stack.popleft()
            if nxt == None:
                return None
            rt = TreeNode(nxt)
            rt.left = get_subtree()
            rt.right = get_subtree()

            return rt

        stack = deque(
            map(
                lambda s: None if s == Codec.NULL_TOKEN else int(s), 
                data.split(Codec.SEPARATOR)
            )
        )

        return get_subtree()


if __name__ == "__main__":
    ser = "1,2,3,null,null,4,5"

    codec = Codec()

    des = codec.deserialize(ser)

    print(des)