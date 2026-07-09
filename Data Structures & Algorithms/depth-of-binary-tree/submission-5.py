# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        stack = [ [root,1] ]
        result = 1

        while stack:

            node, depth = stack.pop()

            if node:

                result = max(result, depth)

                if node.left is not None:
                    stack.append([node.left, depth+1])

                if node.right is not None:
                    stack.append([node.right, depth+1])

        return result


        